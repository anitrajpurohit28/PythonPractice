# 8  Python program to check whether a number is Prime or not


def is_prime(number):
    for i in range(2, number//2):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")


is_prime(11)
is_prime(25)
is_prime(27)
is_prime(23)

