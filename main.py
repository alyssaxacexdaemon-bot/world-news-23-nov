#!/usr/bin/env python3
"""Copy the Tanya Times front page (entry.png) to the Make.fun output directory.

Standard library only. Run with Python 3.13.
"""

import os
import shutil
import sys

ENTRY_NAME = "entry.png"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, ENTRY_NAME)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, ENTRY_NAME)

    shutil.copyfile(source, destination)

    source_size = os.path.getsize(source)
    copied_size = os.path.getsize(destination)
    if copied_size != source_size:
        print(
            f"Size mismatch: copied {copied_size} bytes, "
            f"expected {source_size} bytes",
            file=sys.stderr,
        )
        return 1
    print(f"Copied {source} to {destination} ({copied_size} bytes, verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
