#Draw Square
#Fernando Branco
#CIS129

##Pseudocode
##Lower pen
##Move pen
##Turn LT 90
##Move pen
##Turn LT 90
##Move pen
##Turn LT 90
##Move pen
##Raise pen

from turtle import *
pencolor('red')
speed (10)
for x in range (1,5):
    fd(100)
    lt(90)
up()
lt(180)
fd (80)
down()

###Pseudocode
##Lower pen
##Move pen
##Turn RT 90
##1/2 Move pen
##Turn RT 90
##Move pen
##Turn RT 90
##1/2 Move pen
##Raise pen

pencolor('green')
for x in range (1,5):
    fd(50)
    lt(90)
    fd(25)
up()
lt(90)
fd (100)
down()
lt(90)

###Pseudocode
##Lower pen
##Move forward
##draw square/dot
##Move forward
##draw square/dot
##Move forward
##draw square/dot
## Raise pen

pencolor('black')
for x in range (1,4):
    fd (50)
    dot (5,'blue')
    
up()
rt(90)
fd (20)
down()
pencolor('orange')
fd(100)
up()
back(100)
lt(90)
down ()
fd (50)
up()
back(50)
rt (90)
fd (50)
lt (90)
down()
fd (50)
