def sort(a: list[int]) -> list[int]:
    a1 = a[:len(a)//2]
    a2 = a[len(a)//2:]

    if (len(a1) > 1):
        a1 = sort(a1)
    
    if (len(a2) > 1):
        a2 = sort(a2)

    a_sorted = [0] * (len(a1) + len(a2))

    i = 0
    j = 0

    # make-shift sentinels
    a1.append(max(a2) + 1)
    a2.append(max(a1) + 1)

    for k in range(len(a1) + len(a2) - 2):
        if a1[i] <= a2[j]:
            a_sorted[k] = a1[i]
            i += 1
        else:
            a_sorted[k] = a2[j]
            j += 1
    
    return a_sorted
