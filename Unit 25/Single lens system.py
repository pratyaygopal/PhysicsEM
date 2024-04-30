import numpy as np

u = 72.8
v = 37.5
y1 = 3.44
n = 1.68

x1new = -13.9

flens = 1/((1/v) + (1/u))
print(flens) #Q1

y2 = (u/v)*y1
print(y2*-1) #Q2

rlens = (n - 1) * flens
print(rlens) #Q3

x2new = 1/ ((1/flens) + (1/x1new))
print(x2new) #Q4

print("Virtual and upright")
