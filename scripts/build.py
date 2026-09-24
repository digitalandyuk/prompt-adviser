#!/usr/bin/env python3
"""Build installable Codex and Claude skills from one shared source."""

from pathlib import Path
from shutil import copy2, copytree, rmtree
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
NAME = "prompt-adviser-v2"
DESCRIPTIONS = {
    "codex": "Review ChatGPT, OpenAI and Codex prompts. Score completeness, ask three score-led questions, suggest useful open-source examples and optional Jev, then recommend a model before execution.",
    "claude": "Review Claude prompts. Score completeness, ask three score-led questions, suggest useful open-source examples and optional Jev, then recommend a current Claude model before execution.",
}


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
    header = f'---\nname: {NAME}\ndescription: "{description}"\n---\n\n'
    (folder / "SKILL.md").write_text(header + body + "\n" + appendix)
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
