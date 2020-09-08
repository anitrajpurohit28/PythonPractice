# 2  Python Program for factorial of a number
def fact_0(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_0(n-1)


def fact_1(n):
    return 1 if (n == 1 or n == 0) else n * fact_1(n-1)


def fact_2(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact


num = int(input("Enter the number to find factorial of: "))
result = fact_0(num)
print(f"Factorial of {num} is {result}")


num = int(input("Enter the number to find factorial of: "))
result = fact_1(num)
print(f"Factorial of {num} is {result}")

num = int(input("Enter the number to find factorial of: "))
result = fact_2(num)
print(f"Factorial of {num} is {result}")
