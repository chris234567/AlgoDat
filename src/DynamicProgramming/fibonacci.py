# Through this bottom up implementation the sequence can be calculated in O(n) linear time,
# instead of O(2^n) exponantial time using recursion
def fib(n: int):
    already_computed = {}
    for i in range(n + 1):
        if i == 0:
            already_computed[i] = 0
        elif i == 1:
            already_computed[i] = 1
        else:
            fib = already_computed[i - 1] + already_computed[i - 2]
            already_computed[i] = fib

    return list(already_computed.values())[-1]
