from collections import Counter
from typing import List
import re


def get_longest_diverse_words(file_path: str) -> list[str]:
    with open(file_path, encoding='utf-8', mode='r') as fi:
        file = fi.read().encode('utf-8').decode('unicode-escape')
        words = file.split(' ')
        list_words = sorted(words, key=lambda x: len(set(x)), reverse=True)  #
        list_words = list_words[:10]

    print(list_words)


def get_rarest_char(file_path: str) -> str:
    with open(file_path, encoding='utf-8', mode='r') as file:
        count = Counter(file.read().encode('utf-8').decode('unicode-escape'))  # counts the rarest letters, considering the case
    rarest_char = min(count, key=count.get)
    return rarest_char


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding='utf-8', mode='r') as file:
        text = file.read().encode('utf-8').decode('unicode-escape')
        string_without_letter = re.sub(r'[^!.,?:;\-\(\)\"\"]', '', text)
        quantity = len(string_without_letter)
        return quantity


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, mode='r') as f1:
        file = f1.read().encode('utf-8').decode('unicode-escape')
        a = 0
        for i in file:
            if i.isascii():
                a += 1
        return a


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, mode='r') as f1:
        file = f1.read().encode('utf-8').decode('unicode-escape')
        ascii_simbols = ''
        for i in file:
            if not i.isascii():
                ascii_simbols += i
        count = Counter(ascii_simbols)  # counts the rarest letters, considering the case
        most_common_non_ascii_char = max(count, key=count.get)
        return most_common_non_ascii_char
