def swap(l: list[int], a: int, b: int) -> None:
    temp = l[a]
    l[a] = l[b]
    l[b] = temp