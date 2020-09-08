from random import choice
options = ["rock", "paper", "scissors", "garbage"]
print("...rock...")
print("...paper...")
print("...scissors...")

# === implementation 1 start ===
# for i in range(10):
#     p1 = choice(options)
#     p2 = choice(options)
#     print(f"(enter Player 1's choice): {p1}")
#     print(f"(enter Player 2's choice): {p2}")
#     if p1 == "rock" and p2 == "paper":
#         print("player 2 wins")
#     elif p1 == "rock" and p2 == "scissors":
#         print("player 1 wins")
#     elif p1 == "paper" and p2 == "rock":
#         print("player 1 wins")
#     elif p1 == "paper" and p2 == "scissors":
#         print("player 2 wins")
#     elif p1 == "scissors" and p2 == "rock":
#         print("player 2 wins")
#     elif p1 == "scissors" and p2 == "paper":
#         print("player 1 wins")
#     else:
#         print("draw! same choice")
# === implementation 1 ends ===

# === implementation 2 start ===
# for i in range(10):
#     p1 = choice(options)
#     p2 = choice(options)
#     print(f"(enter Player 1's choice): {p1}")
#     print(f"(enter Player 2's choice): {p2}")
#     if (p1 == "rock" and p2 == "scissors") or\
#        (p1 == "paper" and p2 == "rock") or\
#        (p1 == "scissors" and p2 == "paper"):
#         print("player 1 wins")
#     elif (p1 == "scissors" and p2 == "rock") or\
#          (p1 == "rock" and p2 == "paper") or\
#          (p1 == "paper" and p2 == "scissors"):
#         print("player 2 wins")
#     else:
#         print("draw! same choice")
# === implementation 2 start ===

# === implementation 3 start ===
for i in range(10):
    p1 = choice(options)
    p2 = choice(options)
    print(f"(enter Player 1's choice): {p1}")
    print(f"(enter Player 2's choice): {p2}")
    if p1 == p2:
        print("draw! same choice")
    elif p1 == "garbage" or p2 == "garbage":
        print("Please select rock scissors or paper!")
    else:
        if p1 == "rock":
            if p2 == "scissors":
                print("player 1 wins")
            else:
                print("player 2 wins")
        elif p1 == "paper":
            if p2 == "scissors":
                print("player 2 wins")
            else:
                print("player 1 wins")
        elif p1 == "scissors":
            if p2 == "rock":
                print("player 2 wins")
            else:
                print("player 2 wins")

# === implementation 3 start ===
