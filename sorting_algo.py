########## Bubble Sort # start ################

def bubble_sort(a, size):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]


########## Bubble Sort # end ################

########## Selection Sort # start ################

def selection_sort(a, size):
    for i in range(len(a)):
        pos = i
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                pos = j
        a[pos], a[i] = a[i], a[pos]


########## Selection Sort # end ################


########## Quick Sort # start ################

########## Quick Sort # start ################
def partition2(a, l, r):
    pivot = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def _quick_sort(a, low, high):
    if low >= high:
        return

    # use one of these partition algo
    part = partition1(a, low, high)
    # part = partition2(a, low, high)
    _quick_sort(a, low, part - 1)
    _quick_sort(a, part + 1, high)


def quick_sort(a):
    _quick_sort(a, 0, len(a) - 1)


########## Quick Sort # end ################
def partition1(a, lower_bound, upper_bound):
    pivot = a[lower_bound]
    start = lower_bound+1
    end = upper_bound
    print('Array:', a[lower_bound:upper_bound+1])
    print('Pivot:', pivot)
    print('start:', start, '| a[start]:', a[start])
    print('end:', end, '| a[end]:', a[end])

    while start <= end:
        while start <= end and a[start] <= pivot:
            start += 1
        while start <= end and a[end] > pivot:
            end -= 1
        if start <= end and a[start] > a[end]:
            print(f'{a[start]} <--> {a[end]}')
            a[start], a[end] = a[end], a[start]
    print(f'Pivot swap {a[end]} <--> {pivot}')
    a[lower_bound], a[end] = a[end], a[lower_bound]
    print(a[lower_bound:upper_bound+1])
    print(f'----return {end}:{a[end]}-----')
    return end


def partition2(a, l, r):
    pivot = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def _quick_sort(a, low, high):
    while low >= high:
        return

    # use one of these partition algo
    part = partition1(a, low, high)
    # part = partition2(a, low, high)
    _quick_sort(a, low, part - 1)
    _quick_sort(a, part + 1, high)


def quick_sort(a):
    _quick_sort(a, 0, len(a) - 1)


########## Quick Sort # end ################


########## Heap Sort # start ###############
def heapify(a, size, i):
    large = i
    left = i * 2 + 1
    right = i * 2 + 2

    while left < size and a[left] > a[large]:
        large = left
    while right < size and a[right] > a[large]:
        large = right
    if large != i:
        a[large], a[i] = a[i], a[large]
        heapify(a, size, large)


def heap_sort(a):
    for i in range(len(a) // 2 - 1, -1, -1):
        heapify(a, len(a), i)

    for i in range(len(a) - 1, -1, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)


########## Heap Sort # end ###############


########## Merge Sort # end ###############
def merge(a, l, m, r):
    # can use slice operator for creating
    # left_arr and right_arr
    l_arr = []
    for i in range(l, m + 1):
        l_arr.append(a[i])
    r_arr = []
    for i in range(m + 1, r + 1):
        r_arr.append(a[i])

    i = 0
    j = 0
    k = l  # array A's index.
    while i < len(l_arr) and j < len(r_arr):
        if l_arr[i] < r_arr[j]:
            a[k] = l_arr[i]
            i += 1
        else:
            a[k] = r_arr[j]
            j += 1
        k += 1

    while i < len(l_arr):
        a[k] = l_arr[i]
        i += 1
        k += 1
    while j < len(r_arr):
        a[k] = r_arr[j]
        j += 1
        k += 1


def merge(a, l, mid, r):
    i = l
    j = mid + 1
    k = 0
    # print("arr: ", a[l:r+1]," l: ", l, " mid: ",mid, " r: ",r)
    temp = [0] * (r - l + 1)
    while i <= mid and j <= r:
        if a[i] < a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = a[i]
        i += 1
        k += 1
    while j <= r:
        temp[k] = a[j]
        j += 1
        k += 1

    a[l:r + 1] = temp


def merge_sort(a, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(a, l, m)
        merge_sort(a, m + 1, r)
        merge(a, l, m, r)
########## Merge Sort # end ###############


arr1 = [7, 6, 10, 5, 9, 2, 1, 15, 7]
arr2 = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]

quick_sort(arr1)
print(arr1)

# quick_sort(arr2)
# print(arr2)
