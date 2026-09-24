#!/usr/bin/env python3
"""Send an explicitly approved typed decision request to Jev via OpenRouter."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ENDPOINT = "https://openrouter.ai/api/alpha/decisions"
MODEL = "typesafe/jev-1.13"
KEYCHAIN_SERVICE = "prompt-adviser-openrouter"
KEYCHAIN_ACCOUNT = "prompt-adviser-v2"


def key_from_keychain() -> str | None:
    if sys.platform != "darwin":
        return None
    found = subprocess.run(
        ["security", "find-generic-password", "-w", "-a", KEYCHAIN_ACCOUNT, "-s", KEYCHAIN_SERVICE],
        capture_output=True,
        text=True,
        check=False,
    )
    return found.stdout.rstrip("\n") if found.returncode == 0 else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path, nargs="?", help="JSON file containing state and typed questions")
    parser.add_argument("--send", action="store_true", help="Confirm that this file may be transmitted to OpenRouter and TypeSafe")
    parser.add_argument("--store-key", action="store_true", help="On a Mac, securely prompt for an OpenRouter key and save it in Keychain")
    args = parser.parse_args()

    if args.store_key:
        if args.request or args.send:
            parser.error("--store-key cannot be combined with a request or --send.")
        if sys.platform != "darwin":
            parser.error("--store-key requires macOS; use OPENROUTER_API_KEY on other systems.")
        saved = subprocess.run(
            ["security", "add-generic-password", "-a", KEYCHAIN_ACCOUNT, "-s", KEYCHAIN_SERVICE, "-U", "-w"],
            check=False,
        )
        if saved.returncode == 0:
            print("OpenRouter key saved in macOS Keychain.")
        return saved.returncode

    if args.request is None:
        parser.error("Provide a request file, or use --store-key on a Mac.")

    if not args.send:
        parser.error("No request sent. Add --send only after approving this file for transmission.")

    key = os.environ.get("OPENROUTER_API_KEY") or key_from_keychain()
    if not key:
        parser.error("No OpenRouter key in the environment or macOS Keychain; no request was sent.")

    try:
        payload = json.loads(args.request.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        parser.error(f"Cannot read a JSON request: {exc}")
    if not isinstance(payload, dict) or not isinstance(payload.get("state"), dict) or not isinstance(payload.get("questions"), dict) or not payload["questions"]:
        parser.error("Request must contain a state object and a non-empty questions object.")
    if set(payload) - {"model", "state", "questions"}:
        parser.error("Only model, state and questions are accepted.")
    if payload.get("model", MODEL) != MODEL:
        parser.error(f"This helper only supports {MODEL}.")
    payload["model"] = MODEL

    request = Request(
        ENDPOINT,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=30) as response:
            result = json.load(response)
    except HTTPError as exc:
        print(f"OpenRouter returned HTTP {exc.code}; request content and key were not printed.", file=sys.stderr)
        return 1
    except (URLError, TimeoutError, ValueError) as exc:
        print(f"OpenRouter request failed: {type(exc).__name__}; request content and key were not printed.", file=sys.stderr)
        return 1

    print(json.dumps({"model": result.get("model"), "answers": result.get("answers"), "usage": result.get("usage")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
