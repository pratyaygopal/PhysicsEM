# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#interactive example LC circuit
L = 420
L = L*1/1000
I = 75
I = 75*1/1000
C = 0.05
C = C*(1*1/1000000)
#here we are trold that the energies at time 0 is the same. Since there is no resistors and we treat the inductor as an ideal inductor, there is no resistance in this circuit and thus there is no loss of energy. Therefore we know that the neergy will stay the same. If the energy stays the same, and we are told that they are equal at the start, we can say thie follwoing
#Utotal = 2*Ul
#again, we can do this only because they telll us that the energies are equal. 
#We find the total energy in the system so that we can set that equal to the energy of the capacitor
Ut = 2*(0.5*L*I*I)
#we are told that the instantous current is 75 ma, so we can say that the current at time 0 is 75. 
#When we are at our max charge, current goes to a halt. This goes back to the equations for current and charge in an inductor capcitor circuit. Yes, there are phase angles, but think about it. If Im at a max charge,and my charge is defined by cosine, then my sin must be zero. Just like my will to continue with e and m
Q = (2*Ut*C)**(1/2)
print(Q)

#interactice example LCR Energy
#here the circuit is left open for a really long time
#as a result, the capacitor is like "aight bruh tought shit I aint lietting current go through" whereas the inductor is like a drunk security guard for a bar party and will let anything (even dogs) go through
#we also know that L and C are the only things that can store energy
#so whats the first thing we should do in this situation? Find the current.
#R2 and E4 are in parallel
R1 = 60
R2 = 220
R3 = 330
R4 = 480
C = 250
C = C*1/1000000
V = 9
L = 8
L = L*1/1000
R24 = ((1/R2) + (1/R4))**(-1)
Rt = R24 + R1
I = V / Rt
Ul = 0.5*L*I*I
#so know the question is, how the fuck do we find the voltage of the capaictor?
#well we know current only runs when there is an emf difference. But if the capacitor matches the coltage of the current location, current wont run there. This hinges on the unniversal law of nature that objects or things tend to revert to a state of lower energy at all times when able to do so
V24 = I*R24
I = V24 / R2
Ul = 0.5*L*I*I
Uc = 0.5*C*V24*V24
Ut = Uc + Ul
print(Ut)
