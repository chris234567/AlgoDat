from .sort_utils import swap

def sort(l: list[int]) -> list[int]:
    for i in range(len(l) - 1):
        for r in range(len(l) - 1, i, - 1):
            if l[i] > l[r]:
                swap(l, i, r)

    return l
