# 11  Python Program for How to check if a given number is Fibonacci number?

# Following is an interesting property about Fibonacci numbers that
# can also be used to check if a given number is Fibonacci or not.
# A number is Fibonacci if and only if one or both of
# (5*n2 + 4) or (5*n2 – 4) is a perfect square (Source: Wiki).

import math


def is_perfect_square(num):
    s = int(math.sqrt(num))
    return s*s == num


def is_fibonacci_number(n):
    return is_perfect_square(5*n*n - 4) or is_perfect_square(5*n*n + 4)


for i in range(1, 11):
    if is_fibonacci_number(i):
        print(f"{i} is a fibonacci number")
    else:
        print(f"{i} is NOT a fibonacci number")

