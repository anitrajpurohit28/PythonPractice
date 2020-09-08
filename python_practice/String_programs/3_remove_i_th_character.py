# 3 Ways to remove i’th character from string in Python
input1 = "InputString"
remove_index = 2


def remove_ith_character_naive1(input_str1, remove_index):
    print("------skip copying ith string -------")
    new_str = ""
    for i in range(len(input_str1)):
        if i != remove_index:
            new_str = new_str + input_str1[i]
    return new_str


print(f"Input string: {input1}\tOutput string: "
      f"{remove_ith_character_naive1(input1, remove_index)}")


import string
def remove_ith_character_str_replace(input_str1, remove_index):
    print("------string replace method -------")
    for i in range(len(input_str1)):
        if i == remove_index:
            input_str1 = input_str1.replace(input_str1[i], "")
    return input_str1


new_string = remove_ith_character_str_replace(input1, remove_index)
print(f"Input string: {input1}\tOutput string: "
      f"{new_string}")


def remove_ith_char_slice_concatenate(input_str1, remove_index):
    print("-------slice + concatenate------")
    return input_str1[:remove_index] + input_str1[remove_index+1:]


# slice + concatenate
new_str = remove_ith_char_slice_concatenate(input1, remove_index)
print(f"Input string: {input1}\tOutput string: {new_str}")


# join + list comprehension
def remove_ith_char_join_and_list_comprehension(input_str1, remove_index):
    print("-------join + list comprehension------")
    return ''.join([input1[i] for i in range(len(input1)) if i != remove_index])


new_str = remove_ith_char_join_and_list_comprehension(input1, remove_index)
print(f"Input string: {input1}\tOutput string: {new_str}")




