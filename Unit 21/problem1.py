#this is for the question: Power in an AC circuit
import numpy as np

Em = 120    #v
w = 288     #angular velocity(rad/sec)
L = 0.374     #Henrys
p = 33      #degrees
Pavg = 98   #watt
p = np.deg2rad(p)

#Pavg = 0.5*Imax*Vavg*cosp
Imax = (2*Pavg)/(Em*np.cos(p))
print(Imax)

#Pavg = 0.5*Imax^2*R
R = (2*Pavg)/(Imax*Imax)
print(R)

#tanp = (wL-1/wC)/R

C = 1/(w*w*L-w*R*np.tan(-p))
C = C*10**6                     #accounting for units
print(C)

# for part 4 since current leads the voltage
#1/wC>wL and to achive resonance w must increase
print("w was increased")

#when its in resonance Z = R thus P = 0.5V^2/R

Pres = (Em*Em)/(2*R)
print(Pres)
