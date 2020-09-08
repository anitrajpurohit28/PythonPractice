import random
import time

arr = []
with open("sorted_array.txt", "r") as arr_file:
    arr = [int(element.strip()) for element in arr_file]
    # for element in arr_file:
    #     arr.append(int(element.strip()))
    #print(arr)


def linear_search(inp, key):
    for index in range(len(inp)):
        if inp[index] == key:
            #print(f"Found at index {index}")
            return index
    return -1

def binary_search(inp, key):
    low = 0
    high = len(inp)
    while low <= high:
        mid = (high+low)//2
        #print(f"{mid} -> {inp[mid]}")

        if key == inp[mid]:
            #print(f"found at {mid} index")
            return mid

        if key > inp[mid]:
            low = mid+1
        elif key < inp[mid]:
            high = mid-1
    return -1


print(f"Last element is {arr[-1]}")
# Get the user input
num = int(input("Enter number between to search for: "))
while True:
    # Linear_search
    t1 = time.time()
    ret = linear_search(arr, num)
    if ret != -1:
        print("Element found at {}".format(ret))
    else:
        print("element NOT found")

    t2 = time.time()
    print("Time taken by Linear search: {}".format(t2-t1))


    # binary_search
    t1 = time.time()
    ret = binary_search(arr, num)

    if ret != -1:
        print("Element found at {}".format(ret))
    else:
        print("element NOT found")
    t2 = time.time()
    print("Time taken by binary search: {}".format(t2-t1))

    cont = input("Would you like to continue? [y/n]")
    if cont == 'n':
        break
