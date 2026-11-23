"""news-image-20261123 entry: copy the pre-rendered front page to the
output directory. Python 3.13 standard library only, no network, fully
deterministic: the same input bytes are written on every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    # Fail loudly instead of handing the gate an empty file.
    if os.path.getsize(dest) == 0:
        raise RuntimeError("copied entry.png is empty")
    return 0


if __name__ == "__main__":
    sys.exit(main())
