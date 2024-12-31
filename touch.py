import os
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage touch <filename>")
        return
    argument = sys.argv[1]
    try:
        open(argument, "w")
    except(err):
        print(f"failed to create file, err: {err}")

if __name__ == "__main__":
    main()
