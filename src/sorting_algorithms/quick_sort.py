from .sort_utils import swap

## still a bug somewhere

def partition(l: list, p, r):
    i = p

    for j in range(p, r - 1):
        if l[j] < l[r - 1]:
            swap(l, i, j)
            i += 1
    
    swap(l, i, r - 1)

    return i + 1


def sort(l, p, r):
    if p < r:
        q = partition(l, p, r)

        sort(l, p, q - 1)
        sort(l, q + 1, r)

    return l
