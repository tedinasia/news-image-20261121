#!/usr/bin/env python3
"""Publish the finished front page for 21 November 2026.

The picture itself was drawn ahead of time and ships in this repository
as entry.png. This program only moves it into the grader's output
folder, after checking it is a well-formed PNG inside the size limits.
It uses nothing but the Python standard library, needs no network, and
writes the exact same bytes on every run.
"""
import hashlib
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
BYTE_LIMIT = 1048576
PIXEL_LIMIT = 1024


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def main():
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    target = os.path.join(target_dir, "entry.png")

    with open(SOURCE, "rb") as handle:
        picture = handle.read()

    if len(picture) > BYTE_LIMIT:
        return fail("entry.png is %d bytes, over the 1 MiB limit"
                    % len(picture))
    if picture[:8] != PNG_SIGNATURE:
        return fail("entry.png does not start with the PNG signature")
    if len(picture) < 33:
        return fail("entry.png is too short to hold an IHDR chunk")
    chunk_len = struct.unpack(">I", picture[8:12])[0]
    if picture[12:16] != b"IHDR" or chunk_len != 13:
        return fail("entry.png has no valid 13-byte IHDR chunk")
    width, height = struct.unpack(">II", picture[16:24])
    if width > PIXEL_LIMIT or height > PIXEL_LIMIT:
        return fail("image is %dx%d, over the 1024x1024 limit"
                    % (width, height))

    os.makedirs(target_dir, exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(picture)
    with open(target, "rb") as handle:
        copied = handle.read()
    if copied != picture:
        return fail("the copy in the output folder differs from entry.png")

    digest = hashlib.sha256(picture).hexdigest()
    print("wrote %s: %dx%d PNG, %d bytes, sha256=%s"
          % (target, width, height, len(picture), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
