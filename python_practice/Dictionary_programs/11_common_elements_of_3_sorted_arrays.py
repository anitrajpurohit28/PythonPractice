# 11 Python | Find common elements in three sorted arrays by dictionary intersection

from collections import Counter

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]


def common_elements_counter(ar1, ar2, ar3):
    # output of Counter will be dictionary
    print("common_elements_counter")
    ar_dict1 = Counter(ar1)
    ar_dict2 = Counter(ar2)
    ar_dict3 = Counter(ar3)
    intersect_dict = dict(ar_dict1 & ar_dict2 & ar_dict3)
    print(intersect_dict)

    # create and return the list
    list1 = []
    for key in intersect_dict.keys():
        list1.append(key)

    return list1


def common_elements_set(ar1, ar2, ar3):
    print("common_elements_set")
    s1 = set(ar1)
    s2 = set(ar2)
    s3 = set(ar3)

    intersect_set = s1.intersection(s2, s3)
    print("set intersection:", intersect_set)

    # create and return the list
    list1 = []
    for value in intersect_set:
        list1.append(value)

    return list1


def common_elements_naive(ar1, ar2, ar3):
    print("common_elements_naive")
    len1 = len(ar1)
    len2 = len(ar2)
    len3 = len(ar3)
    i, j, k = 0, 0, 0
    common_list = []
    while i < len1 and j < len2 and k < len3:
        if ar1[i] == ar2[j] == ar3[k]:
            common_list.append(ar1[i])
            print(ar1[i], end= " ")
            i += 1
            j += 1
            k += 1
        elif ar1[i] < ar2[j]:
            i += 1
        elif ar2[j] < ar3[k]:
            j += 1
        else:  # ar1[i] > ar2[j] > ar3[k]
            # ar3[k] is the smallest element
            k += 1
    print()
    return common_list


# NOTE: inputs are always sorted lists
print(common_elements_counter(ar1, ar2, ar3))
print(common_elements_set(ar1, ar2, ar3))
print(common_elements_naive(ar1, ar2, ar3))



