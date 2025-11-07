#!/usr/bin/env python3
# SPDX-license-identifier: EUPL-1.2
# Copyright 2025 Marcus Müller
#
import libarchive
import pathlib


def main(path: pathlib.Path, howmany: int = 0) -> None:
    with libarchive.file_reader(str(path)) as archive:
        counter = 0
        for entry in archive:
            print(entry)
            counter += 1
            if howmany and counter >= howmany:
                break


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="read entries from a tape archive (or other libarchive supported format)"
    )
    parser.add_argument(
        "ARCHIVE", type=pathlib.Path, help="Archive (or tape device) to read"
    )
    parser.add_argument(
        "-n",
        "--how-many",
        type=int,
        default=0,
        help="After how many entries stop reading? (0: don't stop before EOF)",
    )
    args = parser.parse_args()
    main(args.ARCHIVE, args.how_many)
