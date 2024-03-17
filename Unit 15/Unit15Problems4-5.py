import numpy as np
#problem 4
#1 a
#2 b the integral is ero since the dot product B*dl = 0
#3 b
#4 g dont just copy answers, theyre different each time.
#you're given the equation
#super position
I1 = 3.6
I2 = 2.7 
n1 =  1650 
n2 =  1350 
pi = np.pi
u0 = 4*pi*10**(-7)
B = 0.5*u0*(n1*I1 + n2*I2)
print(B)
#problem 5
print(0) #answer to part1
#what is the B field inetween?
#think superposition. If I put a rectangle inbetween those to sheilds, I get that 0.5*I*n*u0 + whatever = B
I1 = 3.4
I2 = 5.4
n =  18 / (1/100)
By = -0.5*u0*(I1*n+n*I2)
#part2
print(By)
#part3
#this just reaks
By2 = -0.5*u0*(I1*n-n*I2)
print(By2)
#part 4
#this part also stinks
#find the verticle component and multiply with the respective shit you calculated before
vert = 0.125 #m
intB1 = By*vert
intB2 = By2*vert
print(intB1 + intB2)
#part 5
By3 = 0.5*u0*(-I1*n+n*I2)
print(By3)
#part 6
print(intB1)

