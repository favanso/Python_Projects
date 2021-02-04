#M8 Assignment
'''
Fernando Branco
CIS 129'''

'''
Write the pseudocode for a program that shows the logic for a program that accepts 15 different words from the console or file.  They should be in random order.

The program should accept the 15 words.
The program should then sort the words in alphabetic order(Use built in sort not bubble sort)
The program should then display the words on separate lines'''

##thewords = ['link','zelda','keese','Hinox','Guardian']
thewords=[]
count = 0

#Enter words from a file
filein = open('gamedata.txt','r')
thewords = filein.readlines()


'''
#Enter words from console
for words in range (1,6):
    userinput=input('Please enter a word: ')
    thewords.append(userinput)
    count += 1
'''

#sort words
thewords.sort()

for words in thewords:
    print(words.strip())
