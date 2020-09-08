# 10  Python Program for Fibonacci numbers


def print_fibonacci_numbers(number):
    fib_list = [0, 1]
    for i in range(2, number+1):
        cur_num = fib_list[i-1] + fib_list[i-2]
        fib_list.append(cur_num)

    print(fib_list)


print_fibonacci_numbers(10)
