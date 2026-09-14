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
        text = f.read()
        print(text)
        print("\n---")
    except (FileNotFoundError, PermissionError,
            IsADirectoryError, UnicodeDecodeError) as e:
        print(f"Accessing file '{sys.argv[1]}'")
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return
    f.close()
    print(f"File '{f.name}' closed.")
    write_nsave(text)


def write_nsave(text: str) -> None:
    final_txt = ""
    txt_list = text.splitlines()
    i = 0
    for line in txt_list:
        final_txt += line + "#"
        if i != (len(txt_list) - 1):
            final_txt += "\n"
        i += 1
    print("\n---")
    new_name = input("Enter new file name (or empty):")
    if new_name == "":
        print("Not saving data.")
        return
    try:
        new_file: typing.IO[str] = open(new_name, 'w')
        print(f"Saving data to '{new_name}'")
        new_file.write(final_txt)
    except FileNotFoundError as e:
        print(f"{e}")
        return write_nsave(text)
    print(f"Data saved in file '{new_name}'")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    text_man()
