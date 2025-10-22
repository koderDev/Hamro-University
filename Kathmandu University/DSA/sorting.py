"""Sorting algorithms with a simple benchmarking harness."""

from __future__ import annotations

from random import randint
from typing import Callable, List

Array = List[int]


def bubble_sort(data: Array) -> Array:
    arr = data[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertion_sort(data: Array) -> Array:
    arr = data[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(data: Array) -> Array:
    if len(data) <= 1:
        return data[:]
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    merged: Array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(data: Array) -> Array:
    if len(data) <= 1:
        return data[:]
    pivot = data[len(data) // 2]
    less = [x for x in data if x < pivot]
    equal = [x for x in data if x == pivot]
    greater = [x for x in data if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)


def run_demo() -> None:
    samples = [randint(0, 100) for _ in range(12)]
    algorithms: dict[str, Callable[[Array], Array]] = {
        "Bubble sort": bubble_sort,
        "Insertion sort": insertion_sort,
        "Merge sort": merge_sort,
        "Quick sort": quick_sort,
        "Python sorted": lambda arr: sorted(arr),
    }

    print("Sample data:", samples)
    for name, algo in algorithms.items():
        result = algo(samples)
        print(f"{name:>15}: {result}")


if __name__ == "__main__":
    run_demo()
