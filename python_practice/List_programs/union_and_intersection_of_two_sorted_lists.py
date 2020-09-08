list1 = [1, 2, 2, 3, 3, 3, 4, 5, 5]
list2 = [3, 4, 4, 5, 6, 6, 7, 8, 9]


def union_of_sorted_list(list1, list2):
    union_list = []
    len1 = len(list1)
    len2 = len(list2)
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            union_list.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            union_list.append(list2[j])
            j += 1
        else:
            union_list.append(list1[i])
            i += 1
            j += 1

    while i < len(list1):
        union_list.append(list1[i])
        i += 1
    while j < len(list2):
        union_list.append(list2[j])
        j += 1
    union_list = remove_duplicates(union_list)
    return union_list


def remove_duplicates(list1):
    new_list = []
    for i in range(len(list1)):
        if list1[i] not in new_list:
            new_list.append(list1[i])
    return new_list


union_list = union_of_sorted_list(list1, list2)
print("Union:", union_list)


def intersection_of_sorted_list(list1, list2):
    intersection_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            i += 1
        elif list1[i] > list2[j]:
            j += 1
        else:
            intersection_list.append(list1[i])
            i += 1
            j += 1
    return intersection_list

intersection_list = intersection_of_sorted_list(list1, list2)
print("Intersection:", intersection_list)