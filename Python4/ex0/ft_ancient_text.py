#!/usr/bin/env python3

import sys
import typing


def check_args() -> None:
    if len(sys.argv) != 2:
        raise SyntaxError("Usage: ft_ancient_text.py <file>")


def text_man() -> None:
    try:
        check_args()
    except SyntaxError as e:
        print(f"{e}")
        return
    try:
        f: typing.IO[str] = open(sys.argv[1], 'r')
        print(f"Accessing file '{f.name}'")
        print("---\n")
        print(f.read())
        print("\n---")
    except (FileNotFoundError, PermissionError,
            IsADirectoryError, UnicodeDecodeError) as e:
        print(f"Accessing file '{sys.argv[1]}'")
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return
    f.close()
    print(f"File '{f.name}' closed.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    text_man()
