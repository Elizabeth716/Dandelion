
from collections.abc import Sequence

def check_fibonacci(data: Sequence[int]) -> bool:
    a = 0
    if len(data)>=3:
        for i in range(len(data)-2):
            if data[i]+data[i+1] == data[i+2]:
                a+=1
        if a+2 == len(data):
            return True
        else:
            return False
    else: return False