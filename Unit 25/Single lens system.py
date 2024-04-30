import numpy as np

u = 133
v = 74.8
y1 = 6.57
n = 1.49

x1new = -28.7

flens = 1/((1/v) + (1/u))
print(flens) #Q1

y2 = (u/v)y1
print(y2 -1) #Q2

rlens = (n - 1) * flens
print(rlens) #Q3

x2new = 1/ ((1/flens) + (1/x1new))
print(x2new) #Q4

print("Virtual and upright")
