# 12 Generating random strings until a given string is generated

import random
import string

given_string = "BAC"
possible_char = string.ascii_letters  # + string.digits

match = False
attempt = 0
while not match:
    attempt += 1
    rand_match_char = ""
    for i in range(len(given_string)):
        rand_match_char += random.choice(possible_char)
        print(rand_match_char)
        if rand_match_char[i] == given_string[i]:
            # if len(rand_match_char) == len(given_string): alternative
            if rand_match_char == given_string:
                print(f"pattern found after {attempt} attempt")
                match = True
        else:
            break
