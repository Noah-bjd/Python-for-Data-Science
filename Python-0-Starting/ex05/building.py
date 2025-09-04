import sys


def main():
    """
    Description:
        Analyzes a given text (from command-line argument) and displays
        statistics about its content. It counts and prints the number of:
        - Uppercase letters
        - Lowercase letters
        - Punctuation marks
        - Digits
        - Spaces

    Parameters:
        None explicitly.
        The function expects one command-line argument (the text to analyze).

    Returns:
        None.
        The function prints the analysis results to the console.

    Raises:
        AssertionError: If more than one argument is provided.
    """
    try:
        if len(sys.argv) < 2:
            try:
                print("What is the text to count?")
                inp = sys.stdin.readline()
                if (inp and not inp.endswith("\n")):
                    print()
            except KeyboardInterrupt:
                sys.stdout.write("\nOperation cancelled by user (Ctrl+C).\n")
                sys.exit(0)
            except EOFError:
                sys.stdout.write("\nNo input received (Ctrl+D).\n")
                sys.exit(0)
        elif len(sys.argv) == 2:
            inp = sys.argv[1]
        elif len(sys.argv) > 2:
            raise AssertionError("Too many arguments provided")
        punctuation = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
        digits = spaces = upper = lower = punct = 0
        for char in inp:
            if char.isspace():
                spaces += 1
            elif char.isdigit():
                digits += 1
            elif char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
            elif char in punctuation:
                punct += 1
        print(f"The text contains {len(inp)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punct} punctuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")

    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
