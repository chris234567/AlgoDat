from .sort_utils import swap


def heapify(l: list[int], i: int, heap_size: int) -> list[int]:
    max = i
    left = i * 2 + 1
    right = left + 1

    # Compare value at i to left leaf
    if left <= heap_size and l[i] < l[left]:
        max = left

    # Compare value at i to left leaf
    if right <= heap_size and l[max] < l[right]:
        max = right

    if max != i:
        swap(l, i, max)
        heapify(l, max, heap_size)


def sort(l: list[int]) -> list[int]:
    heap_size = len(l) - 1

    # Build max heap
    for i in range(((len(l)) // 2) - 1, -1, -1):
        heapify(l, i, heap_size)

    for i in range(len(l) - 1, 0, -1):
        # Swap the root element aka the max element with the last leaf 
        # in order to sort max to min from left of the list inward
        swap(l, 0, i)

        # Reduce heap_size in order for the last already sorted element to be ignored
        heap_size -= 1

        # Max-Heapify the now not anymore max heap because of the swap
        heapify(l, 0, heap_size)

    return l
