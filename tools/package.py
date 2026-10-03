#!/usr/bin/env python3
"""Build the distributable skill archive.

    python3 tools/package.py            # writes dist/modelling-paper-writer-<version>.zip
    python3 tools/package.py --list     # print what would be included, and exit

The zip is what you upload to claude.ai (Settings → Capabilities → Skills) or hand to someone
who is not installing from git. It holds the skill and the material it reads at runtime, and
nothing else: no development tooling, no evals, no CI, no quotation report. Everything is
nested under one top-level directory named after the skill, which is what the uploader expects.

Refuses to build if `tools/corpus.py check` fails, so a broken skill cannot be shipped.
"""

import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"

# What the skill needs at runtime, plus the licence and the citation metadata.
INCLUDE_FILES = ["SKILL.md", "LICENSE", "CITATION.cff", "README.md", "CHANGELOG.md"]
INCLUDE_GLOBS = ["references/*.md", "references/corpus/*.md", "references/corpus/papers.csv"]

# Development-only: present in the repository, never in the archive.
EXCLUDE_DIRS = {".git", ".github", ".claude-plugin", "docs", "evals", "tools", "dist",
                "__pycache__"}


def version():
    for line in (ROOT / "SKILL.md").read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("version:"):
            return line.split(":", 1)[1].strip().strip('"')
    sys.exit("SKILL.md frontmatter has no metadata.version")


def members():
    paths = []
    for name in INCLUDE_FILES:
        path = ROOT / name
        if not path.exists():
            sys.exit(f"missing {name}")
        paths.append(path)
    for pattern in INCLUDE_GLOBS:
        found = sorted(ROOT.glob(pattern))
        if not found:
            sys.exit(f"no files matched {pattern}")
        paths += found

    for path in paths:
        rel = path.relative_to(ROOT)
        if set(rel.parts) & EXCLUDE_DIRS:
            sys.exit(f"{rel} is under an excluded directory; fix INCLUDE_GLOBS")
    return paths


def main():
    paths = members()
    if "--list" in sys.argv:
        for path in paths:
            print(path.relative_to(ROOT))
        print(f"\n{len(paths)} files", file=sys.stderr)
        return 0

    if subprocess.run([sys.executable, str(ROOT / "tools" / "corpus.py"), "check"]).returncode:
        sys.exit("corpus.py check failed; not packaging")

    name = ROOT.name
    DIST.mkdir(exist_ok=True)
    out = DIST / f"{name}-{version()}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in paths:
            zf.write(path, Path(name) / path.relative_to(ROOT))
    size = out.stat().st_size / 1024
    print(f"wrote {out.relative_to(ROOT)} — {len(paths)} files, {size:.0f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
