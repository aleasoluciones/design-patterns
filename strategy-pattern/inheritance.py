import random
from abc import ABC, abstractmethod
from typing import List


class Sorter(ABC):
    @abstractmethod
    def sort(self, data: List) -> List:
        pass


class DirectSorter(Sorter):
    def sort(self, data: List) -> List:
        return sorted(data)

class ReverseSorter(Sorter):
    def sort(self, data: List) -> List:
        return sorted(data, reverse=True)

class RandomSorter(Sorter):
    def sort(self, data: List) -> List:
        return random.sample(data, k=len(data))


data = [5, 8, 2, 1, 9]


direct_sorter: Sorter = DirectSorter()
print(direct_sorter.sort(data))

reverse_sorter: Sorter = ReverseSorter()
print(reverse_sorter.sort(data))

random_sorter: Sorter = RandomSorter()
print(random_sorter.sort(data))

