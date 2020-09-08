# 16 Check if binary representations of two numbers are anagram

num1a, num1b = 5, 6
num2a, num2b = 18, 15

# print("{0}=> {0:010b}".format(num1a))
# print("{0}=> {0:010b}".format(num1b))
# print("{0}=> {0:010b}".format(num2a))
# print("{0}=> {0:010b}".format(num2b))


def check_binary_anagram_format_string_sort(inp1, inp2):
    # First 0 is filler
    # next 10 is the width specifier, till which 0 will be filled
    bin_no1 = "{0:010b}".format(inp1)
    bin_no2 = "{0:010b}".format(inp2)
    # print("sorted bin1:", sorted(bin_no1))
    # print("sorted bin2:", sorted(bin_no2))
    if sorted(bin_no1) == sorted(bin_no2):
        return True
    return False


def check_binary_anagram_naive(inp1, inp2):
    bin1 = bin(inp1)[2:] # to strip off 0b from the binary
    bin2 = bin(inp2)[2:]
    zero_prepend = abs(len(bin1) - len(bin2))
    if len(bin1) < len(bin2):
        bin1 = zero_prepend*'0' + bin1
    else:
        bin2 = zero_prepend*'0' + bin2
    if sorted(bin1) == sorted(bin2):
        return True
    return False

def check_binary_anagram_sorted_str_join(num1, num2):
    bin1 = "{0:08b}".format(num1)
    bin2 = "{0:08b}".format(num2)
    # print("".join(sorted(bin1)), "".join(sorted(bin2)))
    bin1 = "".join(sorted(bin1))
    bin2 = "".join(sorted(bin2))
    if bin1 == bin2:
        return True
    return False


from collections import Counter
def check_binary_anagram_counter(num1, num2):
    bin1 = "{0:08b}".format(num1)
    bin2 = "{0:08b}".format(num2)
    dict1 = Counter(bin1)
    dict2 = Counter(bin2)
    if dict1 == dict2:
        return True
    return False

print(f"inp1: {num1a} -> {bin(num1a)[2:]}")
print(f"inp2: {num1b} -> {bin(num1b)[2:]}")
ret = check_binary_anagram_format_string_sort(num1a, num1b)
print("check_binary_anagram_format_string_sort: ", ret)
ret = check_binary_anagram_naive(num1a, num1b)
print("check_binary_anagram_naive: ", ret)
ret = check_binary_anagram_sorted_str_join(num1a, num1b)
print("check_binary_anagram_sorted_str_join: ", ret)
ret = check_binary_anagram_counter(num1a, num1b)
print("check_binary_anagram_counter: ", ret)

print()
print(f"inp1: {num2a} -> {bin(num2a)[2:]}")
print(f"inp2: {num2b} -> {bin(num2b)[2:]}")
ret = check_binary_anagram_format_string_sort(num2a, num2b)
print("check_binary_anagram_format_string_sort: ", ret)
ret = check_binary_anagram_naive(num2a, num2b)
print("check_binary_anagram_naive: ", ret)
ret = check_binary_anagram_sorted_str_join(num2a, num2b)
print("check_binary_anagram_sorted_str_join: ", ret)
ret = check_binary_anagram_counter(num2a, num2b)
print("check_binary_anagram_counter: ", ret)
