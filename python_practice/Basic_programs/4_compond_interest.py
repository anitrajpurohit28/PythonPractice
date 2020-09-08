# 4  Python Program for compound interest


def compound_interest(p, t, r):
    return p * pow((1 + r / 100), t)


principle = float(input("Principal: "))
time = float(input("Time: "))
rate = float(input("Rate: "))

ci = compound_interest(principle, time, rate)
print(f"Compound interest is {ci}")
