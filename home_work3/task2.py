import time
import struct
import random
import hashlib
import multiprocessing

def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1,3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))

def modified_calculate(number):
    with multiprocessing.Pool(25) as p:
        enum = p.map(slow_calculate, number)
        return sum(enum)



def main():
    start = time.time()
    print(modified_calculate(range(500)))   # output 1024259
    print(time.time() - start)          # output 48.20191216468811

if __name__ == "__main__":
    main()