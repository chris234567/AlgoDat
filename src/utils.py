from random import randint
from typing import List

from utils import Tree, Node


def generate_random_array(n: int):
    a = n * [0]

    for i in range(n):
        a[i] = randint(1, 10)

    return a


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

