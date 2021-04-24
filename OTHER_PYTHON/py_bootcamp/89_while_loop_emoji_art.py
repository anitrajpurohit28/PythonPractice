#print("\U0001f600")

# for i in range(11):
#     print("\U0001f600"*i)

# i = 1
# while i < 11:
#     print("\U0001f600" * i)
#     i += 1

# 90 STOP copy me

# break_string = "stop copying me"
# while True:
#     input_str = input()
#     if input_str == break_string:
#         print("UGH FINE YOU WIN")
#         break
#     else:
#         print(input_str)

# msg = input()
# while msg != "stop copying me":
#     print(msg)
#     msg = input()
# print("UGH FINE YOU WIN")



# 93 guessing game

# version 1
# import random
# res = random.randint(1, 10)
# repeat = "y"
#
# while repeat == "y":
#     inp = int(input("Guess a number between 1 and 10: "))
#
#     if inp > res:
#         print("Too high, try again!")
#     elif inp < res:
#         print("Too low, try again!")
#     else:  # inp == res
#         print("You guessed it! You won!")
#         repeat = input("Do you want to keep playing? (y/n): ")
#         if repeat == "n":
#             break


# Version 2
# import random
# res = random.randint(1, 10)
#
# while True:
#     inp = int(input("Guess a number between 1 and 10: "))
#
#     if inp > res:
#         print("Too high, try again!")
#     elif inp < res:
#         print("Too low, try again!")
#     else:  # inp == res
#         print("You guessed it! You won!")
#         repeat = input("Do you want to keep playing? (y/n): ")
#         if repeat == "y":
#             res = random.randint(1, 10)
#             inp = None
#         else:
#             print("Thank you for playing")
#             break
