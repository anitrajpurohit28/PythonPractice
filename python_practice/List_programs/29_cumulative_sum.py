import random
list1 = [random.randrange(0, 50, 10) for i in range(5)]
print(list1)

cum_list = []

index = -1
while index < len(list1)-1:
    index += 1
    if index == 0:
        cum_list.append(list1[index])
    else:
        cum_list.append((list1[index] + cum_list[index-1]))


print(cum_list)
