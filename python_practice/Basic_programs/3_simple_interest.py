# 3  Python Program for simple interest


def simple_interest(p, t, r):
    return (p * t * r) / 100


principle = float(input("Principal: "))
time = float(input("Time: "))
rate = float(input("Rate: "))

si = simple_interest(principle, time, rate)
print(f"simple interest is {si}")
