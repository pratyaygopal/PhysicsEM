
# Online Python - IDE, Editor, Compiler, Interpreter
import numpy as np 
pi = np.pi 
u0 = 4*pi*10**(-7)
#do IL cross B 
I = 3.4
L = 3.64
B = 5.4
F = I*L*B 
print(F)
#the last calculation part
I1 = 4.84
I2 = 2.2 
d = 7.4 
F = u0*I1*I2 / (2*pi*d)
print(F)
#problem 7 
#find the B field applied on ad, which with the right hnd rule should point you downwards
#do another righ hand rule for the equation
#you should know the equation for biosavart
#part 1
H = 0.36 
W = 0.72 
I1 = 0.726 
I2 = 0.346 
L = 0.35
Bfield1 = u0*I1 / (2*pi*L)
F = Bfield1 * I2 * H
print(F)
#part2
Bfield2 = u0*I1 / (2*pi*(L+W))
Fbc = -Bfield2 * I2 * H
print(Fbc)
#its zero bc I guessed. No jkjk do the right hand rule and realize that the forces are the same magnitude
print(0)
#along the positive y directions
I3 = Bfield2 * (2*pi*2*L) / (u0)
print(I3)
