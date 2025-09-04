import sys


def AlphaCheck(string: str) -> bool:
    """
    Check if the input string contains only alphanumeric characters and spaces.
    """
    try:
        strings = string.split()
        for item in strings:
            assert item.isalnum()
        return True
    except Exception:
        return False


def MorseEncoding(string: str) -> str:
    """
    Encode an alphanumeric string into Morse code.

    Usage:
        python3 morse.py "<string>"

    Example:
        python3 morse.py "Hello 123"
        Output: ".... . .-.. .-.. --- .---- ..--- ...--"
    """
    NESTED_MORSE = {
        'A': '.-',   'B': '-...',  'C': '-.-.',  'D': '-..',
        'E': '.',    'F': '..-.',  'G': '--.',   'H': '....',
        'I': '..',   'J': '.---',  'K': '-.-',   'L': '.-..',
        'M': '--',   'N': '-.',    'O': '---',   'P': '.--.',
        'Q': '--.-', 'R': '.-.',   'S': '...',   'T': '-',
        'U': '..-',  'V': '...-',  'W': '.--',   'X': '-..-',
        'Y': '-.--', 'Z': '--..',  '0': '-----', '1': '.----',
        '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }
    morse_str = ''
    for i, c in enumerate(string.upper()):
        if c in NESTED_MORSE:
            morse_str += NESTED_MORSE[c]
            if i != len(string) - 1:
                morse_str += ' '
    return morse_str


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        assert AlphaCheck(sys.argv[1]), "the arguments are bad"
        strings = sys.argv[1].split()
        code = [MorseEncoding(item) for item in strings]
        print(" ".join(code))
    except Exception as e:
        print(f"AssertionError: {e}")
