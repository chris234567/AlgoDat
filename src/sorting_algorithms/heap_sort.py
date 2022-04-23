from .sort_utils import swap


def build_max_heap(a: list):
    # move from last parent node to first
    index_of_last_parent = int(len(a)/ 2)

    for i in range(index_of_last_parent, 1, -1):
        max = i

        # check if children are smaller
        if a[i] < a[i * 2]:
            max = a[i * 2]
            
        elif a[i] < a[i * 2 + 1]:
            max = a[i * 2 + 1]

        if max != i:
            swap(a, i, max)
            

        else:
            # move to next parent
            return

    return


def heapify(a: list, i):
    max = i - 1

    if a[i - 1] < a[(i * 2) - 1]:
        max = (i * 2) - 1
        
    elif a[i - 1] < a[(i * 2 + 1) - 1]:
        max = (i * 2 + 1) - 1

    # check if max changed
    if max != i - 1:
        swap(a, i - 1, max)
        a = heapify(a, max)

    return a


def sort(a: list):
    #a_max_heap = build_max_heap(a)
    a_max_heap = a
    a_sorted = len(a) * [0]

    for i in range(1, len(a_max_heap) + 1):
        # take out max elem
        a_sorted[-i] = a_max_heap[0]
        a_max_heap[0] = a_max_heap[-1]
        a_max_heap = a_max_heap[:-1]

        # heapify
        a_max_heap = heapify(a_max_heap, 1)

    return a_sorted


print(sort([1, 9, 4, 3, 6, 4, 5]))
