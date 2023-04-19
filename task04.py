from typing import List

def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    totalizer = 0
    for i in A:
        for j in B:
            for k in C:
                for l in D:
                    if i+j+k+l ==0:
                        totalizer +=1
    return totalizer
"""
we use the for loop to iterate over each element in
the array and at the same time we have a condition that
the program checks, and if it is true,
then the value of the totalizer variable becomes more by 1
"""