import urllib.request

def count_dots_on_i(url: str) -> int:
    with urllib.request.urlopen(url) as html:
        read = html.read()
        text: str = read.decode("utf - 8")
        count = text.count('i')
        return count