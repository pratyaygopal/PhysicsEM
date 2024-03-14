
import numpy as np
#sup bitches its ya boy
#on spring break but studying like a mf rn
#problem 2, interactive example
#here we're asked to find the x component of the magnetic field is 
#based on the angle, we know it has to be negative
# int(B*ds) = Ienc * U0
#We can say that B will be constant so we can pull it out of the integral
#this is where it gets a bit funky
#we know that the small wire is just I*u0 / (2pi*r) for the magentic field
#the big where is where it gets a bit weird
#in the lecture slides, they claim that to find the magnetic field inside a wire, to take the ratio of the surface area where the surface area of the actual wire goes as the denominator and the surface area of whatever the fuck you want goes as the numerator
#This would bean that the B field is u0*I*(c-r) / (2*pi*(c-b)**2)
pi = np.pi
I1 = 1.2 #amps, this is the current of the interior
a = 0.02 #m
b = 0.04
c = 0.06
r = 0.05
I2 = 2.4 #amps, this is the current of the exterior wire
#ok here goes nothing
u0 = 4*pi*10**(-7)
B1 = I1 * u0 / (2*pi*r)
B2 = u0*I2*pi*(r**(2)-b**(2)) / ((pi*(c**(2)-b**(2))*2*pi*r))
B3 = B1 - B2
#read this carefully, there are currents going in opposite directions! This is why we subtract them. We denote the postive current as outside of the screen
B = -B3*np.cos(np.deg2rad(30+90)) #I was too lazy to put in the angle for varialbes bc this shit the same anyways
#why 120? because the B field is perpendicular to the r vector
print(B)

#problem 3 Magnetic Fields from Currents in a Wire and a Cylindrical Shell
#part 1
#ok here we're asked to find the y component of the magnetic field at point P. Since this basically has the whole current. There seems to be two things carrying current, the shell and the wire (which are going in opposite directiions)
#since we enscaplte both we can do this
#oh first lemme define variables
a = 0.055
b = 0.08
I1 = 3.4
I2 = 7.3
P = 0.35
T = 0.064
#it asks for the y component but B field is perpenfcular to the radius
#so we only get the y component here
ByP = u0 * (I2-I1) / (2*pi*P)
print(ByP)
#part2 Imma be real this problem is a straight scam
#this asks to find the integral from S to P of B dot dl
#It seems you only get a quarter circle. Furthermore, from R to S the dot product is zero because dl/ds is perpendilcar to B which means this shit zero
#we got ByP is the B field, and multiple that by the circumference of a quarter circle
intByp = 0.25*ByP*pi*P
print(intByp)
#part 3
#this part is just painful. You're probably wondering why I did all the spooky stuff in the interactive exampke. This is because you do the ratios of the surface area. Why surface area? This goes back to the defintion of current (if you dont remeber this even slightly then you may be cooked)
I2enc = I2*pi*(T**2 - a**2) / ((pi*(b**2 - a**2)))
ByT = (I2enc - I1) * (u0 / (2*pi*T))
print(ByT) #side note the sign fo the answer is flipped and I dont know why. Oh nvm basically the I2 is going up because remember that the directions are flipped. 
#Oart 4 is the same as part 2. Remember, integrals only care about where you start and where you end. 
#Part 5 is "remains the same". The answer came to me in a dream and I most defintely did not chegg it out of laziness. 
