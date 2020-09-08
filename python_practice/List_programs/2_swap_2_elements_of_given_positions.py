# 2 Python program to swap two elements in a input_list

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p1 = 2
p2 = 5


def swap_positions_comma_assignment(input_list, pos1, pos2):
    input_list[pos1], input_list[pos2] = input_list[pos2], input_list[pos1]


print(given_list)
swap_positions_comma_assignment(given_list, p1, p2)
print(given_list)

print("--------------")


def swap_positions_pop_insert(input_list, pos1, pos2):
    first_element = input_list.pop(pos1)
    # pop 'pos2-1' because one element is already popped
    # position changed
    second_element = input_list.pop(pos2-1)

    input_list.insert(pos1, second_element)
    input_list.insert(pos2, first_element)


print(given_list)
swap_positions_pop_insert(given_list, p1, p2)
print(given_list)

print("--------------")


def swap_position_using_tuple(input_list, pos1, pos2):
    get = input_list[pos1], input_list[pos2]
    input_list[pos2], input_list[pos1] = get


print(given_list)
swap_position_using_tuple(given_list, p1, p2)
print(given_list)

print("--------------")
