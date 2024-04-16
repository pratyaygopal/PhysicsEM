#this is for the question: AC Circuit 2
import numpy as np

Em = 120  #V
w = 515# * (180/np.pi)  #rad/sec
R = 147  #Ohm
C = 555 * 10**-6  #microfarad
phi = 51 * (np.pi/180) #degrees

t1 = phi/w
print(t1)

Z = R/np.abs(np.cos(phi))
print(Z)

Xc = 1/(w*C)
Xl = R*np.tan(phi) + Xc
L = Xl/w
print(L * 10**3) #for mH

Imax = Em/Z
Vl_max = Imax * Xl
print(Vl_max)

Vl = Vl_max * np.cos(phi)
print(Vl)

print("The value of C would need to be decreased")
