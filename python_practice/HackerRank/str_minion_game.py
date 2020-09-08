def minion_game(string):
    # your code goes here
    stuart = 0  # consonants
    kevin = 0  # vowels
    vowels = "aeiou"
    string = string.lower()

    for i in range(len(string)):
        # print("-"*20)
        # print(string[i])
        if not string[i].isalpha():
            continue
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
