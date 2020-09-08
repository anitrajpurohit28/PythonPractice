# 16 Python | Check if a given string is binary string or not
input1 = "110001010100101010010111"
input2 = "111991902392321923423456543"

print("----is_binary_string_set---")
def is_binary_string_set(input_str):
    bin_set = set("01")
    # OR bin_set = {'0', '1'}

    input_set = set(input_str)

    if input_set == bin_set or \
       input_set == {"0"} or \
       input_set == {"1"}:
        print("Binary string")
    else:
        print("Not a binary string")


is_binary_string_set(input1)
is_binary_string_set(input2)

print("----is_binary_string_char_check---")
def is_binary_string_char_check(input_str):
    bin_str = "01"
    binary_flag = True

    for char in input_str:
        if char not in bin_str:
            binary_flag = False
            break
        else:
            pass

    if binary_flag == True:
        print("Binary string")
    else:
        print("Not a binary string")

is_binary_string_set(input1)
is_binary_string_set(input2)