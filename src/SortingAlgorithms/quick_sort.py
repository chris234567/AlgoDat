from .sort_utils import swap

def sort(l: list[int], p: int, r: int) -> list[int]:
    # Only sort lists with more than one element.
    # Lists with 1 or 0 elements are already sorted.
    if p < r:
        # Use most right position of list as pivot element
        x = l[r]
        i = p

        for j in range(p, r):
            # Sort array relative to pivot
            if l[j] <= x:
                swap(l, i, j)
                i += 1
        
        # Position pivot between the two sorted partial lists
        swap(l, i, r)

        # Recursively sort lists left and right to pivot element
        # with new pivots smaller (l) or greater (r) than the current one 
        sort(l, p, i - 1)
        sort(l, i + 1, r)

    return l
