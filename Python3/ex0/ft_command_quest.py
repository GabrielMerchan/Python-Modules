#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    length = 0
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    length = len(sys.argv)
    if length <= 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {length}")
        i = 1
        while i < length:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
