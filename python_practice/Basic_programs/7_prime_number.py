# 7  Python program to print all Prime numbers in an Interval


def print_prime_number_0(start, end):
    for value in range(start, end+1):
        temp = value//2 + 2
        for n in range(2, value//2 + 2):
            if value % n == 0:
                break
            elif n == value//2+1:
                temp2 = value//2+1
                print(value)


def print_prime_number_1(start, end):
    for value in range(start, end+1):
        for n in range(2, (int(value/2) + 1)+1):
            # +1 because loop ends by end -1
            # int(value/2) + 1 because to and one to mid point of value.
            if value % n == 0:
                break
            elif n == int(value/2)+1:
                print(value)


def print_prime_number_2(start, end):
    for value in range(start, end+1):
        for n in range(2, value//2+2):
            if value % n == 0:
                break
        else:
            print(value)


def print_prime_number_3(start, end):
    for value in range(start, end+1):
        for n in range(2, value//2+2):
            if value % n == 0:
                break
            elif n == value//2+1:
                print(value)


start_range = int(input("Start range: "))
end_range = int(input("End range: "))
print_prime_number_0(start_range, end_range)
print("------")
print_prime_number_1(start_range, end_range)
print("------")
print_prime_number_2(start_range, end_range)
print("------")
print_prime_number_3(start_range, end_range)

