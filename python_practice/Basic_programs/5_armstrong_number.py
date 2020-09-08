# 5  Python Program to check Armstrong Number


def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)


def no_of_digits(num):
    count = 0
    while int(num) != 0:
        num /= 10
        count += 1
    return count


def is_armstrong_number(number):
    no_digits = no_of_digits(number)
    result = 0
    temp = number
    while temp != 0:
        reminder = temp % 10
        result = result + power(reminder, no_digits)
        temp = int(temp/10)

    return result == number


print(f"153 is Armstrong number: {is_armstrong_number(153)}")
print(f"120 is Armstrong number: {is_armstrong_number(120)}")
print(f"1253 is Armstrong number: {is_armstrong_number(1253)}")
print(f"1634 is Armstrong number: {is_armstrong_number(1634)}")
