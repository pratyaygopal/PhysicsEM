
import numpy as np
#wassup fuckers
#its ya boy
#Big D MH HAGOOGI
# resonant frequency is deonated is 1/swrt LC 
C = 470
C = C*(10**-6)
C2 = 321
C2 = C2*(10**-6)
L = 362 
L = L*(10**-3)
Imax = 249
Imax = Imax*(10**-3)
Ctot = ((1/C) + (1/C2))**(-1)
w = 1/(((L*Ctot))**(1/2))
print(Ctot)
print(w)
#this is what we did here
#we can try and solve for the Q max here
pi = np.pi
Qmax = Imax / w*-1
#this means we have a phase shift of pi/2
Q = Qmax * np.cos(w*(30.5*(10**-3)) + pi/2)
print(Q)
#voltage across an inductor is essentially just L*di/dt
#we found Qmax
#lets find dI/dt
dIdt = -w*w*Qmax*np.cos(w*(30.5*(10**-3)) + pi/2)
V = L*dIdt
print(V)
print(Qmax)
#the last one is d 
#if current starts out at a maximhm, the rate of change must be zero. As such, Vl is zero, and so is Q. 
