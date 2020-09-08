# 5 Find length of a string in python (4 ways)

input1 = "InputString"
print(f"len of {input1}: {len(input1)}")

# for loop
def find_length_for(input1):
    count = 0
    for char in input1:
        count += 1
    return count


print(f"len of {input1}: {find_length_for(input1)}")


# while loop
def find_length_while(input1):
    count = 0
    while len(input1) > count:
        count += 1
    return count


print(f"len of {input1}: {find_length_while(input1)}")
