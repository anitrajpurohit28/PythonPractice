for i in range(2, 13):
    for j in range(1,13):
        print("{0:>2} times {1} is {2}".format(j, i, i*j))
    print("-"*40)

with open("sample.txt", 'a') as jabber_poem:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{0:>2} times {1} is {2}".format(j, i, i*j), file=jabber_poem)
        print("-"*20, file=jabber_poem)
