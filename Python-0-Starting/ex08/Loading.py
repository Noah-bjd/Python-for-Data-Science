def ft_tqdm(lst: range) -> range:
    """
    A generator function that mimics tqdm, displaying a progress bar
    as elements from the iterable are yielded.
    Args:
        lst (range): The iterable to process.
    Yields:
        element of the iterable, while updating the progress bar.
    """
    total = len(lst)
    for i, elem in enumerate(lst, 1):
        progress = int((i / total) * 100)
        bar_length = 100
        filled_length = int(bar_length * i // total)
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)
        print(f"\r{progress}%|{bar}| {i}/{total}", end="")
        yield elem
