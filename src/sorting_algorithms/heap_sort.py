from sort_utils import swap


def build_max_heap(l: list):
    for i in range(len(l) // 2, 1, -1):
        heapify(l, i, len(l))


def heapify(l: list, i, last):
    max = None
    left = (i * 2) - 1
    right = (i * 2 + 1) - 1

    # Left leaf
    if left <= last and l[i] < l[left]:
        max = left

    # Right lead 
    elif right <= last and l[i] < l[right]:
        max = right

    if max:
        swap(l, i, max)
        heapify(l, last, max)


def sort(l: list):
    build_max_heap(l)

    for i in range(len(l) - 1, 1, -1):
        # "Take out" max elem or move to end aka sort
        swap(l, 0, i)

        # heapify
        l = heapify(l, 0, i)

    return l


print(sort([1, 6, 2, 4, 5, 8, 3 , 4, 3]))
