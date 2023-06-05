"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
from pathlib import Path
from typing import Optional, Callable


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    total_count = 0
    for file_name in os.listdir(dir_path):
        if file_name.endswith(file_extension):
            file_path = os.path.join(dir_path, file_name)
            with open(file_path) as file:
                if tokenizer:
                    count = sum(len(tokenizer(line)) for line in file)
                else:
                    count = sum(1 for line in file)
                total_count += count
    return total_count
    pass
