# 18 Python program to find uncommon words from two Strings

def uncommon_words(str1, str2):
    count = {}

    # insert words from str1 to hash
    for word in str1.split():
        count[word] = count.get(word, 0) + 1

    # insert words from str2 to hash
    for word in str2.split():
        count[word] = count.get(word, 0) + 1

    return [word for word in count if count[word] == 1]


A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

a = "apple banana mango"
b = "banana fruits mango"

# Print required answer
print(uncommon_words(A, B))
print(uncommon_words(a, b))
