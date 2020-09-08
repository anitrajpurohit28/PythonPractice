# Random string generator

import random
import string

no_of_char = 8

rand_string = ""
for x in range(no_of_char):
    rand_string += random.choice(string.ascii_letters +
                                 string.digits)
print(rand_string)


rand_string = "".join(random.choice(string.ascii_letters + string.digits) for x in range(no_of_char))
print(rand_string)
