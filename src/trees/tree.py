from __future__ import annotations

class Tree:
    def __init__(self, root: Node = None) -> None:
        self.root = root


class Node:
    def __init__(self, key: int, parent: Node = None, right: Node = None, left: Node = None) -> None:
        # Node Value
        self.key = key
        
        # Pointer
        self.parent = parent
        self.right = right
        self.left = left