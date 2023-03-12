def fib(n):
    prev_1 = 0
    prev_2 = 1
    curr = 0
    for _ in range(n):
        curr = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = curr

    return curr
