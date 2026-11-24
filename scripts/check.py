#!/usr/bin/env python3
"""Check package structure and key safety invariants without dependencies."""

from pathlib import Path
from datetime import date
import json
import re
import hashlib
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
NAME = "prompt-adviser"
shared_body = (ROOT / "src/SKILL.template.md").read_text()
release = json.loads((ROOT / "release.json").read_text())
version = release["version"]
assert re.fullmatch(r"\d+\.\d+\.\d+", version), "Invalid release version"
release_date = date.fromisoformat(release["release_date"])
release_label = f"Version {version} · Released {release_date.day} {release_date:%B %Y}"
manifest = json.loads((ROOT / "dist/release-manifest.json").read_text())
assert manifest["version"] == version and manifest["release_date"] == release_date.isoformat()
editions = {"codex": "Codex", "claude": "Claude", "antigravity": "Google Antigravity"}
assert set(manifest["editions"]) == set(editions)
assert f"Current release: **{version}**, {release_date.day} {release_date:%B %Y}." in (ROOT / "README.md").read_text()
assert (ROOT / "CHANGELOG.md").read_text().splitlines()[2] == f"## {version} — {release_date.isoformat()}"
for platform in ("codex", "claude", "antigravity"):
    folder = ROOT / "dist" / platform / NAME
    skill = (folder / "SKILL.md").read_text()
    assert skill.startswith(f"---\nname: {NAME}\ndescription: ")
    assert "Only a direct user instruction to `Run this prompt`" in skill
    assert "In a normal interactive review round, ask exactly three" in skill
    assert "4. Shall I ask more?" in skill
    assert "at least 80%" in skill
    assert "separate, directory-specific" in skill
    assert "No role" in skill
    assert "the finished copyable prompt, last" in skill
    assert (folder / "references/prompt-sources.md").is_file()
    assert (folder / "references/prompting-guidance.md").is_file()
    assert (folder / "references/jev.md").is_file()
    assert (folder / "integrations/jev_openrouter.py").is_file()
    assert (folder / "examples/jev-routing.json").is_file()
    assert "Confirm current OpenRouter compatibility" in skill
    assert f'metadata:\n  version: "{version}"\n  release_date: "{release_date.isoformat()}"' in skill
    assert skill.count(release_label) == 1
    assert f"# Prompt Adviser\n\n{release_label}\n" in skill
    assert f'  edition: "{editions[platform]}"' in skill
    identity = release_label + f"\nEdition: {editions[platform]}"
    assert shared_body in skill.replace("\n" + identity + "\n", "")
    assert (folder / "references/workflow-prompts.md").is_file()
    published = manifest["editions"][platform]
    assert published["edition"] == editions[platform]
    assert published["skill_sha256"] == hashlib.sha256((folder / "SKILL.md").read_bytes()).hexdigest()
    assert (ROOT / f"src/platform-{platform}.md").read_text() in skill
    for reference in (ROOT / "references").iterdir():
        assert (folder / "references" / reference.name).read_bytes() == reference.read_bytes()
    compile((folder / "integrations/jev_openrouter.py").read_text(), "jev_openrouter.py", "exec")
    archive = ROOT / "dist" / f"{NAME}-{platform}.zip"
    assert published["archive"] == archive.name
    assert published["archive_sha256"] == hashlib.sha256(archive.read_bytes()).hexdigest()
    with ZipFile(archive) as zf:
        assert zf.testzip() is None
        names = set(zf.namelist())
        assert f"{NAME}/SKILL.md" in names
        assert all(name.startswith(f"{NAME}/") for name in names)
        assert not any("__MACOSX" in name or ".DS_Store" in name for name in names)
        for item in folder.rglob("*"):
            if item.is_file():
                member = str(Path(NAME) / item.relative_to(folder))
                assert zf.read(member) == item.read_bytes()
    if platform == "codex":
        assert (folder / "agents/openai.yaml").is_file()
    else:
        assert not (folder / "agents").exists()

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.suffix == ".zip":
        continue
    data = path.read_text(errors="ignore")
    assert ("/" + "Users/") not in data, path
    assert re.search(r"ts_[A-Za-z0-9]{20,}", data) is None, path

assert sorted(path.name for path in (ROOT / "dist").glob("*.zip")) == [
    f"{NAME}-{platform}.zip" for platform in sorted(("codex", "claude", "antigravity"))
], "Unexpected release archive in dist"
for platform in ("codex", "claude", "antigravity"):
    assert [path.name for path in (ROOT / "dist" / platform).iterdir()] == [NAME], platform
for path in (ROOT / "README.md", ROOT / "src/SKILL.template.md", ROOT / "src/openai.yaml"):
    data = path.read_text()
    assert " V2" not in data and "-v2" not in data, path

print("Release checks passed: all three skills, archives, references and public text")
