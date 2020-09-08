# 22 Execute a String of Code in Python

code1 = """
a = 6+5
print(a)
"""

code2 = """ 
def factorial(num): 
    fact=1 
    for i in range(1,num+1): 
        fact = fact*i 
    return fact 
print(factorial(5)) 
"""

def exec_code(str):
    exec(str.strip())


exec_code(code1)
exec_code(code2)
