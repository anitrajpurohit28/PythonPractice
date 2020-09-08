# 3 Python program to remove Nth occurrence of the given word

input_list = ["one", "two", "three", "four", "five",
              "one", "two", "three", "four", "five", ]


def remove_nth_occurrence(input_list, input_word, n):
    occurrence = 0

    for i in range(0, len(input_list)):
        if input_list[i] == input_word:
            occurrence += 1
            if occurrence == n:
                del input_list[i]
                return True
    return False


#print(input_list)
flag = remove_nth_occurrence(input_list, 'one', 2)
if flag:
    print(f"Updated list is: {input_list}")
else:
    print("Item not found")

print("------------------")


def remove_nth_occurrence_new_list(input_list, input_word, n):
    new_list = []
    count = 0

    for word in input_list:
        if word == input_word:
            count += 1
            if count == n:
                pass
            new_list.append(word)
        else:
            new_list.append(word)

    if count == 0:
        print("Item not found")
    else:
        print("Updated list is:", new_list)


remove_nth_occurrence_new_list(input_list, 'one', 2)