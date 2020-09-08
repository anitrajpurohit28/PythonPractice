# 5. Python Program to Split the array and add the first part to the end

input1 = [10, 20, 30, 40, 50, 60, 70]
rotate_no = 2

def array_rotation_naive(arr, rotate_no):
    print("array_rotation_naive")
    print("Input:  {}".format(arr))
    length = len(arr)
    for i in range(rotate_no):
        x = arr[0]
        for j in range(i, length-1):
            arr[j] = arr[j+1]
        arr[length-1] = x
    print("output: {}".format(arr))


input1 = [10, 20, 30, 40, 50, 60, 70]
rotate_no = 2

array_rotation_naive(input1, rotate_no)


def array_rotation_split(arr, rotate_no):
    print("array_rotation_split")
    print("Input:  {}".format(arr))
    pre = arr[:rotate_no]
    arr = arr[rotate_no:]+pre
    print("output: {}".format(arr))


input1 = [10, 20, 30, 40, 50, 60, 70]
rotate_no = 2
array_rotation_naive(input1, rotate_no)
