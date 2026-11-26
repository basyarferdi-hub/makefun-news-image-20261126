"""Entry for make.fun bounty: Sum up 26 November's world news in one image.

Copies the bundled entry.png -- a one-page collage of the world news of
Thursday 26 November 2026 -- to entry.png in the output directory.
Deterministic: every run writes exactly the same bytes.
No network access, no dependencies beyond the standard library.
"""

import shutil
import sys
from pathlib import Path


def target_path() -> Path:
    if len(sys.argv) > 1:
        # Optional explicit target, used for local testing only.
        return Path(sys.argv[1])
    grader_dir = Path("/output")
    try:
        grader_dir.mkdir(parents=True, exist_ok=True)
        probe = grader_dir / ".write_probe"
        probe.write_text("", encoding="utf-8")
        probe.unlink()
        return grader_dir / "entry.png"
    except OSError:
        local = Path("output")
        local.mkdir(parents=True, exist_ok=True)
        return local / "entry.png"


def main() -> None:
    src = Path(__file__).resolve().with_name("entry.png")
    dst = target_path()
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
