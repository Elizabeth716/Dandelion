from typing import List

nums = [6, 2, 3, 20, 13]

k = 3

def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    result = 0
    while k>0:
        Maximum = max(nums)
        result = result + Maximum
        nums.remove(Maximum)
        k -= 1
    return result
"""
the while loop for a subarray greater than k executes a code that looks for the maximum
element in the array, and after finding it, writes the value to the result variable, summing
it with the previous value. Next, this element is removed from the array, and the search for
the maximum element continues until k becomes equal to 0
"""