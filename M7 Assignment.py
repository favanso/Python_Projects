#M7 Assignment
#Fernando Branco
#CIS 129

'''Pseudocode
start
Open file
Read file
Get user question
randomnly pick saying from the file data
display to user
end'''

import random
import time

filein = open('EightBData.txt','r')
sayings = filein.readlines()
gametag = input ('Please enter your gametag: ')
while True: 
    input ('Ask me something: ')
    print ('contacting oracle.')
    time.sleep(1)
    print ('contacting oracle..')
    time.sleep(1)
    print ('contacting oracle...')
    time.sleep(1)
    print('Your answer',gametag, 'is ',random.choice(sayings))
    userInput = input('Do you want to ask another question (Y or N to quit):')
    if (str.upper(userInput) == 'N'):
        break
        
print ("Ok, I'm Done")
