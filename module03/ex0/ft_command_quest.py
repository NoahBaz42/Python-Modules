#!/usr/bin/env python3
import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")

    print("Program name:", sys.argv[0])
    size = len(sys.argv[1:])
    if not size:
        print("No arguments provided!")
    else:
        print(f"Arguments recieved: {size}")
        i: int = 1
        while i <= size:
            print(f"Argument {i}:", sys.argv[i])
            i += 1
    print(f"Total arguments: {len(sys.argv)}")
    print()


if __name__ == "__main__":
    ft_command_quest()
