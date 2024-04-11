import numpy as np
#LC CIRCUIT II
R1 = 396
L1 = 354
L1 = L1 * (10**-3)
L2 = 178 * (10**-3)
V = 12
C = 165
C = C*(10**-6)
t1 = 5.15
t1 = t1*(10**-3) #THIS TIME IS FOR PART 4
#so here the switch as been closed, and then is opened. Our capactiro is fully charged and we go to being an LC circuit
#we're asked to find the energy stored in the inductor right aftger the energy is opened
#we know theyll have the same voltage, since theyre connected in parallel. 
#There are two inductors
#So what do we do here?
#Well the equation for the energy of an inductor is
#0.5*L*I*I
#So how do we find the current at the very beginning?
#Our sweet savory boy Cockoff comes to the rescue
#Lets do cockoff on the first loop and then second loop
#you should see that the capactior must be zero. If thats the case, if we left the switch closed for a long time, and it is uncharged, this means that no current had been running through that area. If it had, then there would be some charge on the capactior. The instant the switch is opened therefore, we know its just the max current from the resistor running throiugh the system
#[art 1]
I1 = V / R1
U1 = 0.5*L1*I1*I1
print(U1)
#remember, resonance frequency 1/sqrt(LC)
#if inductors are in series, we add them. I dont know why but it just works I suppose
#part 2
Ltot = L1 + L2
w = 1/((C*Ltot)**0.5)
print(w)
#part 3
#so now we're asked to find the maximum charge when the switch is opened
#so since we assume that these are ideal inductors, there is no resistance, so the current kinda seesaws. 
#Remember, if charge is at a max, current is zero. But wait a minute, we cant use the Qmax equation. We need to use the current equation for LC cirutis
Qmax = I1 / w
print(Qmax*(10**6))
#So why does this work??
#This works because we discoveered that there is a phase shift of pi/2. If we start at the maximum current, then we know that our charge will start off at zero. Why does this physically occur? I couldnt fucking tell you to save my life. 
#So now that we have Qmax, we can use the charge equation now that we know what the phase shift is. We're asked to find the charge at Q1
pi = np.pi
Q1 = Qmax*(np.cos(w*t1+0.5*pi))
print(Q1*(10**6))
#energy is maximzed when charge is maximzed. When is charge maximzed? When cosine is 1. If we have a phase shift of pi*0.5, then w * t must also equal that. So what we area really finding is w*t = pi*0.5
t2 = pi*0.5 / w
print(t2*(10**3))
#for the last one the energy is zero. If charge is maximzed, then current is zero. If current is zero there is no energy sotred in the inducotrs. 
#thats it, thanks for coming to my ted talk

