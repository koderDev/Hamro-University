"""Singly linked list implementation with common operations."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Iterator, Optional


@dataclass
class Node:
    value: Any
    next: Optional["Node"] = None


class SinglyLinkedList:
    def __init__(self, values: Optional[Iterable[Any]] = None) -> None:
        self.head: Optional[Node] = None
        if values is not None:
            for value in values:
                self.append(value)

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        cursor = self.head
        while cursor.next:
            cursor = cursor.next
        cursor.next = new_node

    def prepend(self, value: Any) -> None:
        self.head = Node(value, next=self.head)

    def remove(self, value: Any) -> bool:
        if not self.head:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        prev = self.head
        cursor = self.head.next
        while cursor:
            if cursor.value == value:
                prev.next = cursor.next
                return True
            prev, cursor = cursor, cursor.next
        return False

    def __iter__(self) -> Iterator[Any]:
        cursor = self.head
        while cursor:
            yield cursor.value
            cursor = cursor.next

    def __repr__(self) -> str:
        values = " -> ".join(str(value) for value in self)
        return f"SinglyLinkedList({values})"


if __name__ == "__main__":
    numbers = SinglyLinkedList([1, 2, 3])
    numbers.append(4)
    numbers.prepend(0)
    print("List after insertions:", list(numbers))

    numbers.remove(2)
    print("After removing 2:", list(numbers))

    removed = numbers.remove(99)
    print("Attempted removal of 99:", removed)
