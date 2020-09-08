# 4 Python | Check if a Substring is Present in a Given String

input_string = "This is a input string"
sub_str = "input"

if input_string.find(sub_str) == -1:
    print("Str not found")
else:
    print("Str found")

if input_string.count(sub_str) == 0:
    print("Str not found")
else:
    print("Str found")

