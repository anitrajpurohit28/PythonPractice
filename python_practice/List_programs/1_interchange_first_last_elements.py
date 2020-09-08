# 1 Python program to interchange first and last elements in a list

print("-----1------")
def swap_list_using_temp1(input_list):
    temp = input_list[0]
    input_list[0] = input_list[-1]
    input_list[-1] = temp


my_list = [1, 2, 3, 4, 5, 6, 7]
swap_list_using_temp1(my_list)
print(my_list)

print("-----2------")
def swap_list_using_temp_len(input_list):
    length_of_list = len(input_list)

    temp = input_list[0]
    input_list[0] = input_list[length_of_list - 1]
    input_list[length_of_list - 1] = temp


my_list = [1, 2, 3, 4, 5, 6, 7]
swap_list_using_temp_len(my_list)
print(my_list)

print("-----3------")
def swap_list_using_tuple_variable(input_list):
    # Storing the first and last element
    # as a pair in a tuple variable get
    get = input_list[0], input_list[-1]
    # unpacking tuple elements
    input_list[-1], input_list[0] = get


my_list = [1, 2, 3, 4, 5, 6, 7]
swap_list_using_tuple_variable(my_list)
print(my_list)


print("-----4------")
def swap_list_using_push_pop(input_list):
    curr_element = input_list.pop()
    input_list.insert(0, curr_element)


my_list = [1, 2, 3, 4, 5, 6, 7]
swap_list_using_push_pop(my_list)
print(my_list)


print("-----5------")
def swap_list_using_star_oper_tuple(input_list):
    # In this function, input arg is modified but not reflected
    # into calling function hence we are returning the value
    # to calling function
    start, *mid, last = input_list
    # print(start, mid, last)  # 1 [2, 3, 4, 5, 6] 7
    # By copying the variable directly into variable input_list,
    # input_list will turn into tuple
    # Now, input_list is a tuple; its not a list anymore
    input_list = last, *mid, start
    # print(input_list)
    # calling function will get the right value only if
    # this function returns and calling function will receive it
    return input_list


# list property will be lost by this method
my_list = [1, 2, 3, 4, 5, 6, 7]
swap_list_using_star_oper_tuple(my_list)
print(my_list)
my_list = swap_list_using_star_oper_tuple(my_list)
print(my_list)

print("-----6------")
def swap_list_using_star_oper_list(input_list):
    start, *middle, end = input_list
    input_list = [end, *middle, start]
    return input_list


my_list = [1, 2, 3, 4, 5, 6, 7]
swap_list_using_star_oper_list(my_list)
print(my_list)
my_list = swap_list_using_star_oper_list(my_list)
print(my_list)