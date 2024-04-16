#this is for the question:AC Circuit 1
import numpy as np
w = 855
emax = 120
R = 71
C = 12*10**-6
L = 72.5*10**-3
#calculate the impedance of the inductor and the capacitor
xL = w*L
xC = 1 / (w*C)
#this is based on the cyclical anture of the circuit denoted by omega
z = ((R**2) + (xL-xC)**2)**0.5
print(z)
#impdenace is defined by omega of the circuit, not omega naught. Why is this the case? Could not fucking tell you
#to find the max current I multiply the impedance by the max emf. Where does this derviation come from? I dont fucking know. 
Im = emax/z
print(Im)
#part 3
#here we are asked to find the phase angle. 
#this requires a bit of drawing but I will guide you through it 
#In the impedance phasor diagram, your xL will be at a maxium before it has even started moving. This comes down to the trig of where these impedences start. I frgot what functions the impedence and capcitor follow youll just have to follow
#xL is at the postive y axis and xC is at th negative Y axis
#resistance is on the postive y axis. I then do a verticle line from my resitance line and then draw the impedence arrow. 
#for more info follow this link to see how to do tis problem . https://smart.physics.illinois.edu/Course/PlaySlideshow?unitItemID=318583&enrollmentID=133067
#first calculate xL-xC
xtot = xL - xC
print(xtot, "this is meant to see if the current is dragging by its balls or leading with its dick, its not an answer")
degree1 = np.arctan(xtot / R)
degree = np.rad2deg(-degree1)   
rad1 = np.rad2deg(degree)
print(degree)
#part 4
#here we're asked to find the voltage across the inductor when its zero after a time interval of zero
#the voltage across the inductore is just emf*sin(wt)
#this is what you would think but this is a lie
#remember, the voltage across the inductor is L*di/dt. But di/dt is defined by sin(wt-phi) 
#we calculated a phase angle of 28. something
w1 = w*(180/np.pi)
t = (90 - degree) / w1
print(t)
#for whatever reason you dont calculate anything using radians. idk why
print("a")
#to do number 6 we must understand the following. to find the voltage of the capactior at its max, we know that impdence is maximuzed when the trig is 1. so 1/wC
VmaxC = -xC * Im
#so the preclecutre fucking lies to you. The maximum voltage across the capcitor gets magnified some how and I dont know why
Vct = -VmaxC*np.cos(rad1)
print(Vct)
