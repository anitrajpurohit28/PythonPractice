# 1 Python | Sort Python Dictionaries by Key or Value
input_dict = {2: 64, 1: 69, 4: 23, 5: 65, 6: 34, 3: 76}
print(input_dict)

print("---- Only keys, sorted ---")
for key in sorted(input_dict):
    print(key, end=" ")
print()
print("---- (Key, value) with keys sorted---")
for key in sorted(input_dict.keys()):
    print("({}: {}) ".format(key, input_dict[key]), end=' ')
print()

print("---- (Key, value) with values sorted---")
# here we are using sorted with key. where key is just swapped tuple object
print(sorted(input_dict.items(), key=lambda kv: (kv[1], kv[0])))
# OR
def key_fun(key_value_pair):
    return key_value_pair[1], key_value_pair[0]
print(sorted(input_dict.items(), key=key_fun))

print("--- ordered dictionary ---")

from collections import OrderedDict

dict1 = OrderedDict(sorted(input_dict.items()))
print(dict1)


inp_dict1 = {'ravi': '10', 'rajnish': '9', 'sanjeev': '15', 'yash': '2', 'suraj': '32'}
dict1 = OrderedDict(sorted(dict1.items(), reverse=True))
print(dict1)
dict2 = OrderedDict(inp_dict1.items())
print(dict2)
