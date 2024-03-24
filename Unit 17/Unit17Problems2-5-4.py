#aight wassup fuckers its ya boy skinny penor
#Just kidding its datis. 
#Unit 17 problem 2
#part 1
#this one is kinda cancer
#essentially, the way that this one works is by integration. Youre asked to find what the magnetic flux ix through the loop. We can find this out by first figuring out the equation we're gonna be using. THis is the integral of B * dA. Why an integral? Because there is a current carrying wire who's magtnic field is changing as e move away from it. We know that a magnetic field due to a wire can be found by u0 * I / 2*pi*r. Since the time being asked is t=17 seconds, thsi is where our current isnt changing so we can take the constant current of 5.1 A as our current. We then plug the equation for B into the integral, only to realize we dont have anything for dA. Fear not, Since in this case B field only varies from how FAR away we are from thr wire, the B field only change horizontally. 
#what this means is that W, the width of the sqaure is held constant. this means that dA can be written as W * dr, where dr is the unit length we move. BUt hold on, what are our integration bouds? D to D+L. That way dA being dr*W holds true because we're starting from d. It also iportant to note that the flux will be into the screen but they're asking for magnitude so who the fuck cares anymore
import numpy as np
I1 = 5.1
w = 0.35
l = 0.74
d = 0.49
pi = np.pi
u0 = 4*pi*10**(-7)
#integration = int((u0*I1 / 2*pi*r) *W * dr)
#after integration = (u0*I1*w / 2*pi) * (np.log(d+L) - np.log(d))
flux = ((u0*I1*w) / (2*pi)) * (np.log((d+l) / (d)))
print(flux)
#part 2
#later on in the shizo post Ill elaborate on something thats been on my mind. Remember that girl from all the way from Novemeber? Yeah. theres been a few developments. 
# induced emf only occurs if something is changing. In this case our current is changing 
#so whwat do we do? Well we know current is changing. And we know our equation for flux last time was ((u0*I1*w) / (2*pi)) * (np.log((d+l) / (d))). All we do is replace I1 with dI/dt as it is changing here. 
dIdT = 5.1 / 17
#we then just multiply it by the area
emf1 = ((u0*(dIdT)*w) / (2*pi)) * (np.log((d+l) / (d)))
print(-emf1)
#anyways so there was this girl and I noticed something strange. Typically, I only really have cruses that last 2 months and I either snap outo f it and realize they were never fit for me or that I try and ask them out and its 50/50. But this girl is different. Not only have I had a crush on her for 6 wholeass months, but the feeling never went away. I kept trying to ask myself why this was. Why was it that it was for this particular person? And why hadnt I done anything? I began to ponder, and I think I have an naswer Ill get to later in this homework onaswer key
#part 3
#nothing is changing so the answer must be zero
print(0)
#any how I realized that what I had particularly fallen for was her personality. I think one thing that all of us have in common are the following:
#as much as we'd like to sell ourselves short for, everyone of us in the group is extremely talented. However, we know when to let us, and we have the humility to make fun of ourselves and others. A heart, and humility is what I think. We also know how and when to let loose. This is precisely what I had noticed about her. She had the humility to not feel like she was constantly uptight and had humility. Furthermore, it didn't feel like her actions were behind a veil of abstraction. As depressing as it sounds, I think people are far too obsessed with maitning this image of "perfection" (yes I realize I am guilty of this as well) and try to pander the false standard of perfection. Its addicting to fall into a trap and one that is hard to break the cycle of. 
#part 4
#in this problem the direction will be clockwise as it is the opposing slope to what we had before. 
print("clockwise")
#part 5 we do the samething in part 2 but now its a negative slope
dIdT = -5.1 / (34-28)
emf2 = ((u0*(dIdT)*w) / (2*pi)) * (np.log((d+l) / (d)))
print(-emf2)
#However, I felt like I was in a moral conundrum. At the time, I was os busy with my grades, IEM, and the startup that if I did ask her out, and in the rare chance she did say yes, I would have little to no time to give to her. Additionally, I just felt unsure of if it was even worth it to ask her out. 
#to furthermor add on, I just felt like it would be particularly awkard since we do see each other somewhat often. The last thing Id want to do is make someone feel awkward or uncomfortable
#problem 5 "moving coil"
#For thie problem we're asked to find the force of the thing. To do this, we must find the unduced current first. We can find the direction of the induced current b y doing the right hand rule and by knowing that the unduced current must resist the changing in magnetic field, which is into the screen. Therefore, the current on side W going in to the b field must be going upwards. 
#(vBL / R) to find current. Remember, our thingamabob has a resistance to it
v = 0.05 # m / s 
B = 1.6
w = 0.03
l = 0.08
r = 2
I = (v*B*w / r)
F = I * B * w
print(F)
#as I was saying, I ultimately realzed this that Id like to share with you all
#Through basic texting, it just seems she would reject 100% and just isnt into me. Without having to go into detail, it is what it is. To be quite honest with you, this will happen a lot. You may think you ahve found the right person only to realize that not only have you idealized them beyond the point of recognition, but you've idealized yourself beyond recognition in the process. Often times for first timers, it is easy to loose yourself in trying to find someone else. #This is okay. You will be rejected plenty, but that doesnt mean that you yourself arent worth it to someone. 
#It is certaintly not a pleasent feeling but one that happens. Its how we learn what to do and what not to do. Its how you learn for your exams, you build a repoistory of what to say and what not to say so you can be a better version of yourself next time. 
#Ultiamtely, you as a person are always growing. I think all of us have amazing talents for others to actually apperciate. Its just a matter of finding the right person who will apperciate us for who we are, rather than the idealization they have or we haven given to each other. 
#Though sad, it was a fun while I tried, and at least I can walk away knowing that I tried rather than asking myself "well what if I hadnt asked her to dinner". 
#Until next time, this is the main shizo post. Best of luck to you all
#-TheD00T
#problem 4
#-x, left to right, y, -y, thereis induced current
#double cbeck as we may have different questions
