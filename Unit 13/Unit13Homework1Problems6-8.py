# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#Particle in a magnetic field
#I want to die 
#Lowk though Im looking forward to going home. I feel like I've only been working and not taking time off for myself. On one hand, I really want to do well in my field but you're only young once. 
import numpy as np

#you may have different values but for me it is arrow B for part 1
#remember for negative charges its the opposite direction to what you get with the right hand rule. This is because we use positive test charges for damn near everything (physics contructs :)

#part 2
#force is qv cross B
#I forgor why this is but I put in a proper explaination for why this is soon
q1 = -2.3 #C
v = -2.7 #m/s
B = -2.2
#Since youre crossing B, and B is perpendicular to v, you can tell sin theta to fuck off
force = q1*v*B
print(-force)
#part 3
#another direction question. Again, values may be different but I got the following: into the page
#part 4:
#here we're asked to find the velocity
#it seems in my problem the B and v vectors are perpendicular. Since we're given a root 2 in the denominator, this means our x and y are the same in magnitude

#q*v*B = F
#F / qB === v
q2 = 1.2
force2 = 6.23
B2 = 5.2
velocity = force2 / (q2*B2)
print(velocity)

#problem 6 Motion in a Magnetic Field I
#here w're given the following
#mass of the partile
m = 7.1 * (1/100000000) #kg
B = 3.2
r = 0.87 #meters
t = 799 * (1/1000000)
#here we use cirular motion because somehow it fucking holds with particles smaller than my will to be a mech e major
#but first we need to find velcoity. We can do this by finding the distance traveled and dividing it by the time it took to leave the reigion of which it traveled. From what it seems, the particle travls a quarter circle. We can find the distance by doing pi*r/2
dist = 3.1415926 * r * 0.5
velocity = dist / t
print(velocity)
#this next bit I had a bit of trouble with but heres my best take
#around the circle you are going at a constant velocity
#velcocity can be written as the angle multiple by radius (arc length), divided by the time. We know the radius is 0.87
#v = r*theta / time
#v*time = r*theta
#theta = v*time / r
t1 = 266.3 * (1/1000000)
theta = velocity * t1 / r
#force calucated by circular motin
force = m * velocity * velocity / r
forceX = force * np.cos(theta)
print(-forceX)
forceY = force*np.sin(theta)
print(-forceY)
#we're asked to find the charge. While doing this homewoprk I nearly passed out and I astral projected to Isaac Newton himself and he told me that the charge is negative. Think about it, when you did the right hand rule, you probably said "how the fuck does thsi go in cirular motion?" Well its because its negative so the direction is flipped
#force  = qv cross B
#you know the drill
#force / vB ===charge
charge = force / velocity*B
charge = -1*charge
#fuck off I know I couldve done that in fewer lines. And? 
print(charge*1000000) #just noting this is probably wrong but idgaf
#last problem Motion in a Magnetic Field II
q = 1.6 * (1/10000000000000000000) #how small is this fucking charge?
m = 1.67*(1/1000000000000000000000000000)
D = 0.7
#youre given a block that has an e field
#also because theyre piece of shit they give you the velocity vector in parts
#part 1
vx = 5*100000
vy = 3.4*100000
v = np.array([vx, vy])
v = np.linalg.norm(v)
print(v)
#what the fuck is the point of this question?? Why not just give us the velocity? Anyone with a fucking pulse can do pythagorean. 
#part 2
#just a shitload of shitty trig
# i strongly dislike this
#to find the angle to find R, we use the given angle at where the particle exits
#draw whats happening for a visual of the trig
angle = np.arctan(vy/vx)
R = D / np.sin(angle)
print(R)

#so why the angle? Because youre given D. With the angle that you got, you can use sin to find R
#part 3
#If a business major even looked at this they would die of of sudden death. Maybe putin should show this to business majors he doesnt like so he can actually have a valid claim of not killing someone. 
#find the h cord of the proton?
#you already calcualted the angle for this
#so use it to find h
h = R*np.cos(angle)
h = R - h
print(h)
#find B
#qv cross B ===F
#F/qv = B
#B should be negative
f = m*v*v / R
B = f / (q*v)
print(-B)
#answers appear in sequntial order. 
