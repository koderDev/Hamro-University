"""Linear and binary search utilities with example usage."""

from __future__ import annotations
from typing import Iterable, List, Optional


def linear_search(sequence: Iterable[int], target: int) -> Optional[int]:
    for index, value in enumerate(sequence):
        if value == target:
            return index
    return None


def binary_search(sorted_sequence: List[int], target: int) -> Optional[int]:
    low = 0
    high = len(sorted_sequence) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_sequence[mid] == target:
            return mid
        if sorted_sequence[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5, 6]
    target = 5
    print("Linear search index:", linear_search(numbers, target))

    sorted_numbers = sorted(numbers)
    print("Sorted numbers:", sorted_numbers)
    print("Binary search index:", binary_search(sorted_numbers, target))
