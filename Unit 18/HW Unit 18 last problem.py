import numpy as np

#All resistance variables in ohms

R1 = 56
R2 = 56
R3 = 77
R4 = 133

V = 12
L = 0.296 #in Henrys

#######################################

R134 = R1 + R3 + R4
R23 = 1 / ((1/R2) + (1/R3))
R1234 = R1 + R23 + R4

I40 = V/R134
print(I40) #Q1

I4inf = V / R1234
print(I4inf) #Q2

ILinf = (I4inf * R3) / (R2 + R3)
print(ILinf) #Q3

t = 0.0036 
R32 = R2+R3
exp = -(t * R32) / L

I3inf = ILinf * (np.e ** exp)
print(-I3inf)

VLmaxc  = ILinf*R32
print(VLmaxc)

VLmaxo = I40*R3
print(VLmaxo)