#!/usr/bin/env python3
"""news-image-20261123 v2 — write the entry image to the output directory.

The image is rendered fresh by the builder and stored next to this file as
entry.png. This program only copies those exact bytes to
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png), so repeated runs are
byte-identical. Standard library only; no network.
"""
import os
import shutil
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    size = os.path.getsize(SRC)
    if size == 0:
        print("entry.png is empty, refusing to copy", file=sys.stderr)
        return 1
    shutil.copyfile(SRC, dst)
    if os.path.getsize(dst) != size:
        print("copied file size mismatch", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (dst, size))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
