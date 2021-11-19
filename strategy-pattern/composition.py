import random
from typing import List, Callable


def direct_sort_fn(data: List[int]) -> List[int]:
    return sorted(data)

def reverse_sort_fn(data: List[int]) -> List[int]:
    return sorted(data, reverse=True)

def random_sort_fn(data: List[int]) -> List[int]:
    return random.sample(data, k=len(data))


class Sorter:
    def __init__(self, sorter: Callable[[List[int]], List[int]]):
        self.sorter = sorter

    def sort(self, data: List[int]) -> List[int]:
        return self.sorter(data)


data = [5, 8, 2, 1, 9]


direct_sorter: Sorter = Sorter(direct_sort_fn)
print(direct_sorter.sort(data))

reverse_sorter: Sorter = Sorter(reverse_sort_fn)
print(reverse_sorter.sort(data))

random_sorter: Sorter = Sorter(random_sort_fn)
print(random_sorter.sort(data))

