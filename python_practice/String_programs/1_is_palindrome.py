# 1 Python program to check if a string is palindrome or not

input1 = "malayalam"
input2 = "geeks"
input3 = "12345678987654321"


print("---reversing string---")
def is_palindrome_reverse(input_str):
    rev_str = input_str[::-1]
    if rev_str == input_str:
        return True
    else:
        return False


print(f"input1: {input1} is_palindrome: {is_palindrome_reverse(input1)}")
print(f"input1: {input2} is_palindrome: {is_palindrome_reverse(input2)}")
print(f"input1: {input3} is_palindrome: {is_palindrome_reverse(input3)}")


print("---Iterative string---")
def is_palindrome_iterative(input_str):
    for i in range((len(input_str))//2):
        if input_str[i] != input_str[len(input_str)-1-i]:
            return False
    return True


print(f"input1: {input1} is_palindrome: {is_palindrome_iterative(input1)}")
print(f"input1: {input2} is_palindrome: {is_palindrome_iterative(input2)}")
print(f"input1: {input3} is_palindrome: {is_palindrome_iterative(input3)}")

print("---built-in string---")
def is_palindrome_builtin_reversed(input_str):
    rev_str = ''.join(reversed(input_str))
    if rev_str == input_str:
        return True
    else:
        return False


print(f"input1: {input1} is_palindrome: {is_palindrome_builtin_reversed(input1)}")
print(f"input1: {input2} is_palindrome: {is_palindrome_builtin_reversed(input2)}")
print(f"input1: {input3} is_palindrome: {is_palindrome_builtin_reversed(input3)}")


print("---manually build string and compare---")
def is_palindrome_build_and_compare(input_str):
    rev_str = ''
    for char in input_str:
        rev_str = char + rev_str

    if rev_str == input_str:
        return True
    else:
        return False


print(f"input1: {input1} is_palindrome: {is_palindrome_build_and_compare(input1)}")
print(f"input1: {input2} is_palindrome: {is_palindrome_build_and_compare(input2)}")
print(f"input1: {input3} is_palindrome: {is_palindrome_build_and_compare(input3)}")
