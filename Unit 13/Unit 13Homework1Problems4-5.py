
#I want to fucking jump off al edge
#3/3/2024
import numpy as np
#part 1 of Problem 4
#here we're asked to find the x copnent of the force on the segment ac
#to do this, we know the force will be normal to ca
#therefore, we must find the angle at a
bc = 0.69
ab = 0.13
i = 0.376 #amps
B = 1.17
angle = np.arctan(bc / ab)
angle = np.rad2deg(angle) + 90
print(angle)
length = np.array([ab, bc])
length = np.linalg.norm(length)
force = i*B*length
forcex = force*np.cos(np.deg2rad(angle))
forcey = force*np.sin(np.deg2rad(angle))
print(forcex)
print(forcey)
#here we're asked to find the change in potential energy of the wire
#potential energy of a given wire is u*B*cos(theta)
#while the angle doesnt change the mu component does, lets calulate it
mu1 = i*bc*ab*0.5
mu2 = -mu1
energy1 = mu1*B
energy2 = -mu2*B
energytotal = energy1 + energy2
print(energytotal)

#I want to perish
# in this problem we're asked to find when the proton remerges into the field free reigion
# when the proton goes in, theyll be put in to ciruclar motion
#theyll travel half a circle
#find the force
#qvB
mass = 1.67*(1/1000000000000000000000000000)
charge = 1.6*(1/10000000000000000000)
B = 1.2
velocity = 1*(10*10*10*10*10*10)
force = charge*B*velocity
#mv^2/r = f
radius = (mass*velocity*velocity / force)
dist = (3.14159) * radius
time = dist / velocity
print(time)