#!/usr/bin/env python3
"""Check package structure and key safety invariants without dependencies."""

from pathlib import Path
import re
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
NAME = "prompt-adviser-v2"
for platform in ("codex", "claude"):
    folder = ROOT / "dist" / platform / NAME
    skill = (folder / "SKILL.md").read_text()
    assert skill.startswith(f"---\nname: {NAME}\ndescription: ")
    assert "Only a direct user instruction to `Run this prompt`" in skill
    assert "Always ask exactly three" in skill
    assert "4. Shall I ask more?" in skill
    assert "at least 80%" in skill
    assert "final item" in skill
    assert (folder / "references/prompt-sources.md").is_file()
    assert (folder / "references/jev.md").is_file()
    assert (folder / "integrations/jev_openrouter.py").is_file()
    assert (folder / "examples/jev-routing.json").is_file()
    assert "OpenRouter is a supported route" in skill
    compile((folder / "integrations/jev_openrouter.py").read_text(), "jev_openrouter.py", "exec")
    archive = ROOT / "dist" / f"{NAME}-{platform}.zip"
    with ZipFile(archive) as zf:
        assert zf.testzip() is None
        names = set(zf.namelist())
        assert f"{NAME}/SKILL.md" in names
        assert all(name.startswith(f"{NAME}/") for name in names)
        assert not any("__MACOSX" in name or ".DS_Store" in name for name in names)
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

print("Release checks passed: both skills, archives, references and public text")
