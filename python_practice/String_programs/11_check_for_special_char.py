# 11 Python | Program to check if a string contains any special character

txt1 = "CompanyA12"
txt2 = "andfa322ABGFDASVF"
txt3 = "!@asdesad fx"

print(txt1.isalnum())
print(txt2.isalnum())
print(txt3.isalnum())

print("-----my_isalnum------")
def my_isalnum(string):
    special_char = """'[@_!#$%^"&*()<>?/\\|}{~:]"""
    for char in string:
        if char in special_char:
            return False
        else:
            continue
    return True


print(my_isalnum(txt1))
print(my_isalnum(txt2))
print(my_isalnum(txt3))


print("------search in string.punctuation-----")
from string import punctuation


def my_is_str_alpha_numeric(input_string):
    for char in input_string:
        if char in punctuation:
            return False
        else:
            return True


print(my_is_str_alpha_numeric(txt1))
print(my_is_str_alpha_numeric(txt2))
print(my_is_str_alpha_numeric(txt3))


print("------re module; regex----")
import re
def is_alpha_numeric_regex(input_string):
    regex = re.compile(punctuation)
    if regex.search(input_string):
        return False
    else:
        return True


print(my_is_str_alpha_numeric(txt1))
print(my_is_str_alpha_numeric(txt2))
print(my_is_str_alpha_numeric(txt3))

