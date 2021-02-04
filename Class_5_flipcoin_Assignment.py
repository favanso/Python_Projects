##CIS129
##Fernando Branco
##M4 Assignment: Making Decisions

'''
Pseudocode
Start
Ask for input your name
Display Welcome message and describe program
Generate random number (0 or 1)
if 0 than
Display Heads
else display Tails
Display thank you for playing
Stop
'''

import random
name=""
myrandomnumber = 0
name = input ('Please enter your name: ')
print ('Welcome',name, 'to the Heads and Tails game')
print ('This game simulates flipping a coin')
myrandomname = random.randint(0,1)
if myrandomname == 0:
    print ('You flipped Heads')
else:
    print('You flipped Tails')
print ('Thank you for playing')
