from typing import List, Any, Tuple
from itertools import product


def combinations(*args: List[Any]) -> List[Tuple]:
    all_combinations = product(*args)
    return list(all_combinations)