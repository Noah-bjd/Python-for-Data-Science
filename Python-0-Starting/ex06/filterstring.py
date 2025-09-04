from ft_filter import ft_filter
import sys


def filterString(text: str, number: int) -> str:
    """
    Return a list of words from the string `S` that have a
    length greater than `N`.

    Args:
        S (str): A string containing words separated by spaces.
        N (int): The minimum length threshold.

    Returns:
        list[str]: A list of words longer than `N` characters.

    Raises:
        AssertionError: If the number of arguments is not 2 or if `S` is not a
        string,
                        or `N` is not an integer.
    """
    words = text.split()
    longer_words = list(ft_filter(lambda w: len(w) > number, words))
    return longer_words


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        string = sys.argv[1]
        assert sys.argv[2].lstrip('+-').isdigit(), "the arguments are bad"
        num = int(sys.argv[2].lstrip('+-'))
        result = filterString(string, num)
        print(result)
    except Exception as e:
        print(f"AssertionError: {e}")
