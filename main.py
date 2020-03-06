##For Engineering and Mechanics/POE, by Jpfeif29
##Regardless of the psudo random nature of random number generation on current computers the distrubution should *in theory* be a perfect distrubution
##Baring solar flares of course



import random
import time

print("Select the amount of flips")
times = int(input())

flip = 1
turns = 1
flipper = 1

dieside1 = []
dieside2 = []

print("How many sides?")
turns = int(input())
turns = turns - 1
turnss = turns + 1


while flipper <= turnss:
    dieside1.append(0)
    dieside2.append(0)
    flipper = flipper + 1
    
    time.sleep(.01)
    print(dieside1)
    time.sleep(.01)
    print(dieside2)

while times >= flip:
    
    die1 = random.randint(0, turns) 
    die2 = random.randint(0, turns)
    


    current = dieside1[die1]
    current = current + 1    
    dieside1[die1] = current

    current = dieside2[die2]
    current = current + 1    
    dieside2[die2] = current
    
    
    print("Die 1 is " + str(die1))
    print("Die 2 is " + str(die2))
    print("Flip is " + str(flip))


    flip = flip + 1 

print(dieside1)
print(dieside2)

    
time.sleep(1000)
    
    
