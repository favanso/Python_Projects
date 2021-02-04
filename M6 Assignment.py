#M6 Assignment
#Fernando Branco
#CIS 129

'''Pseudocode
start
Load array with sayings
Get user question
randomnly pick saying
display to user
end'''

import random
import time

sayings = ["As I see it, yes",
"It is certain",
"Most likely",
"Outlook good",
"Without a doubt",
"Yes - definitely",
"You may rely on it",
"Reply hazy, try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Very doubtful",
"Do I Look Like I Care?",
"Yeah, Right",
"Ask Again Later",
"DUH!",]
gametag = input ('Please enter your gametag: ')

while True: 
    input ('Ask me something: ')
    print ('contacting oracle.')
    time.sleep(1)
    print ('contacting oracle..')
    time.sleep(1)
    print ('contacting oracle...')
    time.sleep(1)
    print(random.choice(sayings),', ',gametag)
    userInput = input('Do you want to ask another question (Y or N to quit):')
    if (str.upper(userInput) == 'N'):
        break
        
print ('I`m Done',gametag)
