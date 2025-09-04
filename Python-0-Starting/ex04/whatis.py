import sys

try:
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        sys.exit()
    if not sys.argv[1].lstrip('+-').isdigit():
        raise AssertionError("argument is not an integer")
    num = int(sys.argv[1].lstrip('+-'))
    print("I'm Even." if num % 2 == 0 else "I'm Odd.")
except AssertionError as e:
    print(f"AssertionError: {e}")
