"""Binary Search Tree supporting insert, search, delete, and traversals."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable, Generator, Optional


@dataclass
class _Node:
    key: Any
    left: Optional["_Node"] = None
    right: Optional["_Node"] = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[_Node] = None

    def insert(self, key: Any) -> None:
        def _insert(node: Optional[_Node], key: Any) -> _Node:
            if node is None:
                return _Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            return node

        self.root = _insert(self.root, key)

    def contains(self, key: Any) -> bool:
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def delete(self, key: Any) -> None:
        def _min_value_node(node: _Node) -> _Node:
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node: Optional[_Node], key: Any) -> Optional[_Node]:
            if node is None:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                successor = _min_value_node(node.right)
                node.key = successor.key
                node.right = _delete(node.right, successor.key)
            return node

        self.root = _delete(self.root, key)

    def traverse(self, order: str = "inorder") -> Generator[Any, None, None]:
        visit: Callable[[_Node], Generator[Any, None, None]]

        def inorder(node: Optional[_Node]):
            if node:
                yield from inorder(node.left)
                yield node.key
                yield from inorder(node.right)

        def preorder(node: Optional[_Node]):
            if node:
                yield node.key
                yield from preorder(node.left)
                yield from preorder(node.right)

        def postorder(node: Optional[_Node]):
            if node:
                yield from postorder(node.left)
                yield from postorder(node.right)
                yield node.key

        choices = {
            "inorder": inorder,
            "preorder": preorder,
            "postorder": postorder,
        }
        if order not in choices:
            raise ValueError(f"Unsupported traversal order: {order}")
        visit = choices[order]
        yield from visit(self.root)


if __name__ == "__main__":
    values = [50, 30, 20, 40, 70, 60, 80]
    bst = BinarySearchTree()
    for value in values:
        bst.insert(value)

    print("Inorder traversal:", list(bst.traverse("inorder")))
    print("Contains 60:", bst.contains(60))
    print("Contains 99:", bst.contains(99))

    bst.delete(30)
    print("After deleting 30:", list(bst.traverse("inorder")))
