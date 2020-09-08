# 6  Python Program for Program to find area of a circle

from math import pi


def area_of_circle(radius):
    return pi * radius * radius


r = float(input("Radius: "))
area = area_of_circle(r)
print(f"Area of circle: {area}")
