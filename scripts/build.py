#!/usr/bin/env python3
"""Build installable Codex, Claude and Antigravity skills from one shared source."""

from pathlib import Path
from datetime import date
import json
import re
import hashlib
from shutil import copy2, copytree, rmtree
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
NAME = "prompt-adviser"
RELEASE = json.loads((ROOT / "release.json").read_text())
VERSION = RELEASE["version"]
if not re.fullmatch(r"\d+\.\d+\.\d+", VERSION):
    raise ValueError("release.json version must use major.minor.patch")
RELEASE_DATE = date.fromisoformat(RELEASE["release_date"])
RELEASE_LABEL = f"Version {VERSION} · Released {RELEASE_DATE.day} {RELEASE_DATE:%B %Y}"
DESCRIPTIONS = {
    "codex": "Create or review ChatGPT, OpenAI and Codex prompts from drafts, briefs or conversation. Clarify material gaps, check model fit and finalise before execution.",
    "claude": "Create or review Claude prompts from drafts, briefs or conversation. Clarify material gaps, check thinking-mode fit and finalise before execution.",
    "antigravity": "Create or review Google Antigravity prompts from drafts, briefs or conversation. Clarify material gaps, check model and tool fit and finalise before execution.",
}
EDITIONS = {"codex": "Codex", "claude": "Claude", "antigravity": "Google Antigravity"}


def build(platform: str) -> None:
    folder = DIST / platform / NAME
    if folder.exists():
        rmtree(folder)
    folder.mkdir(parents=True)
    description = DESCRIPTIONS[platform]
    if len(description) > 200:
        raise ValueError(f"{platform} description exceeds 200 characters")
    body = (ROOT / "src/SKILL.template.md").read_text()
    appendix = (ROOT / f"src/platform-{platform}.md").read_text()
    header = (
        f'---\nname: {NAME}\ndescription: "{description}"\n'
        f'metadata:\n  version: "{VERSION}"\n'
        f'  release_date: "{RELEASE_DATE.isoformat()}"\n'
        f'  edition: "{EDITIONS[platform]}"\n---\n\n'
    )
    # Keep the shared instructions intact; insert the human-readable identity
    # after their title so installed files are identifiable without YAML tools.
    title, separator, rest = body.partition("\n")
    if title != "# Prompt Adviser" or not separator:
        raise ValueError("Shared skill must start with its product title")
    identity = RELEASE_LABEL + f"\nEdition: {EDITIONS[platform]}"
    versioned_body = title + "\n\n" + identity + "\n" + rest
    (folder / "SKILL.md").write_text(header + versioned_body + "\n" + appendix)
    copytree(ROOT / "references", folder / "references")
    copytree(ROOT / "integrations", folder / "integrations")
    copytree(ROOT / "examples", folder / "examples")
    if platform == "codex":
        (folder / "agents").mkdir()
        copy2(ROOT / "src/openai.yaml", folder / "agents/openai.yaml")
    archive = DIST / f"{NAME}-{platform}.zip"
    with ZipFile(archive, "w", ZIP_DEFLATED) as zf:
        for path in sorted(folder.rglob("*")):
            if path.is_file():
                info = ZipInfo(str(Path(NAME) / path.relative_to(folder)))
                info.date_time = (1980, 1, 1, 0, 0, 0)
                info.compress_type = ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                zf.writestr(info, path.read_bytes())
    print(f"Built {folder} and {archive}")


if __name__ == "__main__":
    for target in DESCRIPTIONS:
        build(target)
    manifest = {"version": VERSION, "release_date": RELEASE_DATE.isoformat(), "editions": {}}
    for target, label in EDITIONS.items():
        archive = DIST / f"{NAME}-{target}.zip"
        entry = DIST / target / NAME / "SKILL.md"
        manifest["editions"][target] = {
            "edition": label, "archive": archive.name,
            "archive_sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
            "skill_sha256": hashlib.sha256(entry.read_bytes()).hexdigest(),
        }
    (DIST / "release-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
