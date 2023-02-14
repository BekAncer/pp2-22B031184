import math

def area(h,a,b):
    S = (a + b) / 2 * h
    print(S)

print("heigth:")
h = float(input())
print("Base, first value:")
a = float(input())
print("Base, second value:")
b = float(input())
area(h,a,b)