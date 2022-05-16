# Restrict input to list of integers because counting sort can only sort integers
# (or rather objects that can be mapped to a key, but there is no such key() function implemented,
# so it will be integers for now:))
def sort(l: list[int]) -> list[int]:
    k = max(l)
    
    # Initialize counting list with k + 1 positions (+1 because of 0),
    # where c[k] is the max value of the input list
    c = [0] * (k + 1)

    # Count the occurences of certain value in input list l between 0 and k
    # and add it to the corresponding index of c
    for i in l:
        c[i] += 1

    o = []
    
    # Append n apperances of m in input list l m times to output list o
    for i, v in enumerate(c):
        o.extend([i] * v)

    return o