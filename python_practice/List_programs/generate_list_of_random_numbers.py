# Generate list of random numbers

import random

# generate list of random numbers by comprehension + randint
list1 = [random.randint(1, 100) for i in range(10)]
print(list1)

# generate list of random numbers by comprehension + randrange
list1 = [random.randrange(1, 100) for i in range(10)]
print(list1)

# generate list of random numbers by sample
list1 = random.sample(range(1, 100), 10)
print(list1)

# populate list one by one by appending one at a time
list1 = []
for i in range(1, 11):
    list1.append(random.randint(1, 100))
print(list1)

# to generate random numbers in multiples of 10
# with randint
list1 = []
list1 = [random.randint(1, 10) * 10 for i in range(10)]
print(list1)

# with randrange
list1 = []
list1 = [random.randrange(0, 100, 10) for i in range(10)]
print(list1)
