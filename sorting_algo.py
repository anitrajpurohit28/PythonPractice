########## Bubble Sort # start ################

def bubble_sort(a, size):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
########## Bubble Sort # end ################

########## Selection Sort # start ################

def selection_sort(a, size):
    for i in range(len(a)):
        pos = i
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                pos = j
        a[pos], a[i] = a[i], a[pos]

########## Selection Sort # end ################



########## Quick Sort # start ################
def partition1(a, low, high):
    pivot = a[low]
    start = low+1
    end = high

    while start <= end:
        while start <= high and a[start] <= pivot:
            start += 1
        while end >= low and a[end] >= pivot:
            end -= 1
        if start <= end and a[start] > a[end]:
            a[start], a[end] = a[end], a[start]
    a[low], a[end] = a[end], a[low]
    return end


def partition2(a, l, r):
    pivot = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

def _quick_sort(a, low, high):
    while low >= high:
        return

    # use one of these partition algo
    part = partition1(a, low, high)
    # part = partition2(a, low, high)
    _quick_sort(a, low, part-1)
    _quick_sort(a, part+1, high)

def quick_sort(a):
    _quick_sort(a, 0, len(a)-1)

########## Quick Sort # end ################


########## Heap Sort # start ###############


########## Heap Sort # end ###############

arr = [7, 6, 5, 4, 3, 2, 1]
arr = [7, 6, 10, 5, 9, 2, 1, 15, 7]
print(arr)
quick_sort(arr)
print(arr)
#bubble_sort(arr, len(arr))
#selection_sort(arr, len(arr))
