#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate a pure ELF64 hello world program"""


import sys
from warnings import filterwarnings as filter_warnings


def main() -> int:
    """Entry/main function"""

    with open("hello_world", "wb") as bf:
        bf.write(
            b"\x7f\x45\x4c\x46\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x03\x00\x3e\x00\x01\x00\x00\x00\x78\x00\x40\x00\x00\x00\x00\x00\x40\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00\
\x38\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x07\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\x40\x00\
\x00\x00\x00\x00\xa6\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\x00\x00\x00\
\x00\x00\x10\x00\x00\x00\x00\x00\x00\xb8\x01\x00\x00\x00\xbf\x01\x00\x00\x00\
\x48\x8d\x35\x10\x00\x00\x00\xba\x0d\x00\x00\x00\x0f\x05\xb8\x3c\x00\x00\x00\
\x48\x31\xff\x0f\x05\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x0a"
        )

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"

    filter_warnings("error", category=Warning)
    sys.exit(main())
