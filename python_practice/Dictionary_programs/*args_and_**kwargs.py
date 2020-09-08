
def my_fun1(*argv):
    for arg in argv:
        print(arg)
my_fun1("Hello", "welcome", "to", "GeeksForGeeks")

print("---my_fun2---")
def my_fun2(arg1, *argv):
    print("First:", arg1)
    for arg in argv:
        print(arg)
my_fun2("Hello", "welcome", "to", "GeeksForGeeks")

print("---kwargs---")
def my_fun3(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_fun3(first="Geeks", mid="For", last="Geeks")

print("---argv and kwargs---")
def my_fun4(*argv1, **kwargs):
    for arg in argv1:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_fun4("Hello", "world", first="Geeks", mid="For", last="Geeks")
