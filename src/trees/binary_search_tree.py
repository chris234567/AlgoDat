from typing import List

from ..utils import Tree, Node


class Bst_recursive():   
    @staticmethod
    def build_binary_search_tree(l: List[int]) -> Tree:
        T = Tree(
            Node(l[0])
        )

        for k in l:
            Bst_recursive.insert(T, k)
    
    @staticmethod
    def insert(x: Node, key):
        if x.key < key:
            if x.right:
                Bst_recursive.insert(x.right, key)
            else:
                x.right = Node(key)
                x.right.parent = x
        else:
            if x.left:
                Bst_recursive.insert(x.left, key)
            else:
                x.left = Node(key)
                x.left.parent = x

    @staticmethod
    def in_order_tree_walk(x: Node) -> None:
        if x:
            Bst_recursive.in_order_tree_walk(x.left)
            print(x.key)
            Bst_recursive.in_order_tree_walk(x.right)

    @staticmethod
    def search(x: Node, k: int) -> int:
        if x.key == k:
            return x

        elif x.key < k:
            return Bst_recursive.search(x.right, k)

        else:
            return Bst_recursive.search(x.left, k)


    @staticmethod
    def min(x: Node) -> int:
        if not x.left:
            return x

        return Bst_recursive.subtree_min(x.left)

    @staticmethod
    def max(x: Node) -> int:
        if not x.right:
            return x

        return Bst_recursive.max(x.right)

    @staticmethod
    def predecessor(T: Tree, x: Node) -> int:
        return

    @staticmethod
    def successor(T: Tree, x: Node) -> int:
        return

    @staticmethod
    def insert(T: Tree, x: Node) -> int:
        return

    @staticmethod
    def delete(T: Tree, x: Node) -> int:
        return


class Bst_iterative():
    @staticmethod
    def in_order_tree_walk(T: Tree, x: Node) -> None:
        return

    @staticmethod
    def search(T: Tree, x: Node) -> int:
        return

    @staticmethod
    def min(x: Node) -> int:
        while x.left:
            x = x.left
        
        return x

    @staticmethod
    def max(x: Node) -> int:
        while x.right:
            x = x.right
        
        return x

    @staticmethod
    def predecessor(T: Tree, x: Node) -> int:
        return

    @staticmethod
    def successor(T: Tree, x: Node) -> int:
        return

    @staticmethod
    def insert(T: Tree, x: Node) -> int:
        return

    @staticmethod
    def delete(T: Tree, x: Node) -> int:
        return


# Bst_recursive.in_order_tree_walk([2, None, 5, None, None, None, 7, None, None, None, None, None, None, 6, 8, None, None, None, None, None, None, None, None, None, None, None, None, 5], 0)

print(Bst_recursive.min([6, 3, 9, 1, 4, 7]))
print(Bst_recursive.max([6, 3, 9, 1, 4, 7]))
