# 9  Python Program for n-th Fibonacci number


def fibonacci_recursive(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci_recursive(number-1) + fibonacci_recursive(number - 2)


def fibonacci_dyn(number):
    fib_list = [0, 1]
    for i in range(2, number+1):
        cur_num = fib_list[i-1] + fib_list[i-2]
        fib_list.append(cur_num)
    return fib_list[number]


print(f"5: {fibonacci_recursive(5)}")
print(f"6: {fibonacci_recursive(6)}")
print(f"7: {fibonacci_recursive(7)}")
print(f"9: {fibonacci_recursive(9)}")

print('-------')

print(f"5: {fibonacci_dyn(5)}")
print(f"6: {fibonacci_dyn(6)}")
print(f"7: {fibonacci_dyn(7)}")
print(f"9: {fibonacci_dyn(9)}")