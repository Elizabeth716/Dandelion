from typing import List


def fizzbuzz(n: int) -> List[str]:
    list = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            list.append("fizz buzz")
        elif i % 5 == 0:
            list.append("buzz")
        elif i % 3 == 0:
            list.append("fizz")
        else:
            list.append(str(i))
    return list