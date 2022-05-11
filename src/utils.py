from random import randint


def generate_random_array(n: int) -> int:
    a = n * [0]

    for i in range(n):
        a[i] = randint(1, 10)

    return a
