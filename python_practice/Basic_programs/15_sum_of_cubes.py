# 15  Python Program for cube sum of first n natural numbers


def sum_of_squares(num):
    res = 0
    for i in range(1, num+1):
        res = res + (i*i*i)
    return res


number = int(input("Enter a number: "))
result = sum_of_squares(number)
print(f"Sum of squares till {number}: {result}")
