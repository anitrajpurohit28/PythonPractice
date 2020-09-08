# 7 Python | Reversing a List

print("-------reverse iterator---------")
def reverse_itr(input_list):
    return [element for element in reversed(input_list)]


input_lst = list(range(10, 21))
print(input_lst)
reversed_list = reverse_itr(input_lst)
print(reversed_list)


print("-------builtin reverse---------")
def reverse_builtin_reverse(input_list):
    input_list.reverse()


input_lst = list(range(10, 21))
print(input_lst)
reverse_builtin_reverse(input_lst)
print(input_lst)


print("-------iterate reverse, sliced---------")
def reverse_iter_sliced(input_list):
    new_list = input_list[::-1]
    return new_list


input_lst = list(range(10, 21))
print(input_lst)
reversed_list = reverse_iter_sliced(input_lst)
print(reversed_list)