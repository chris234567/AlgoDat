from this import d
from turtle import left


def in_order_tree_walk(l: 'list[int]', i: int) -> None:
    # Avoids index out of bounds because of "short circuiting"
    if i < len(l) and l[i]:
        left = i * 2 + 1
        right = i * 2 + 2

        in_order_tree_walk(l, left)
        print(l[i])
        in_order_tree_walk(l, right)


in_order_tree_walk([2, None, 5, None, None, None, 7, None, None, None, None, None, None, 6, 8, None, None, None, None, None, None, None, None, None, None, None, None, 5], 0)


class Bst_recursive():
    @staticmethod
    def in_order_tree_walk(l: 'list[int]', i: int) -> None:
        # Avoids index out of bounds because of "short circuiting"
        if i < len(l) and l[i]:
            left = i * 2 + 1
            right = i * 2 + 2

            in_order_tree_walk(l, left)
            print(l[i])
            in_order_tree_walk(l, right)

    @staticmethod
    def search(l: 'list[int]', i: int) -> int:
        return

    @staticmethod
    def min(l: 'list[int]') -> int:
        left = 0

        while left < len(l):
            i = left
            left = i * 2 + 1

        return l[i]


    @staticmethod
    def max(l: 'list[int]') -> int:
        return

    @staticmethod
    def predecessor(l: 'list[int]', i: int) -> int:
        return

    @staticmethod
    def successor(l: 'list[int]', i: int) -> int:
        return

    @staticmethod
    def insert(l: 'list[int]', i: int) -> int:
        return

    @staticmethod
    def delete(l: 'list[int]', i: int) -> int:
        return


class Bst_iterative():
    @staticmethod
    def in_order_tree_walk(l: 'list[int]', i: int) -> None:
        return

    @staticmethod
    def search(l: 'list[int]', i: int) -> int:
        return

    @staticmethod
    def min(l: 'list[int]') -> int:
        return

    @staticmethod
    def max(l: 'list[int]') -> int:
        return

    @staticmethod
    def predecessor(l: 'list[int]', i: int) -> int:
        return

    @staticmethod
    def successor(l: 'list[int]', i: int) -> int:
        return

    @staticmethod
    def insert(l: 'list[int]', i: int) -> int:
        return

    @staticmethod
    def delete(l: 'list[int]', i: int) -> int:
        return


print(Bst_recursive.min([6, 3, 9, 1, 4, 7]))
