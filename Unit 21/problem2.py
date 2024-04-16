#this is for the question: AC Circuit in Resonance
import numpy as np

em = 24
w = 143
Imax = 0.57 
C = 157 * (10**(-6))#mFarads

L = (1 / ((w * w) *C)) * 1000
print(L) #Q1

Umax = (1/2) * (L) * (Imax * Imax) * (10 ** -3)
print(Umax) #Q2

Pavg = (1/2) * em * Imax
dU = Pavg * ((2 * 3.14)/w)
print(dU) #Q3

Q = (Umax/dU) * 2 * 3.14
print(Q) #Q4

R = em/Imax 
print(R) #Q5

print("Q Decreases") #Q6
