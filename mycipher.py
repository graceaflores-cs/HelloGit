import sys

def shift_char(c, n):
    # Shift uppercase A–Z by n with wraparound
    return chr((ord(c) - ord('A') + n) % 26 + ord('A'))

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    shift = int(sys.argv[1])

    # Read all input from stdin
    text = ""
    for line in sys.stdin:
        text += line.upper()

    # Keep only A–Z
    filtered = [c for c in text if 'A' <= c <= 'Z']

    # Apply shift
    encoded = [shift_char(c, shift) for c in filtered]

    # Print in blocks of 5 letters, 10 blocks per line
    count = 0
    for c in encoded:
        print(c, end="")
        count += 1

        # space every 5 letters
        if count % 5 == 0:
            print(" ", end="")

        # newline every 50 letters (10 blocks)
        if count % 50 == 0:
            print()

    print()  # final newline

if __name__ == "__main__":
    main()

