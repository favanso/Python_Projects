#Turtle Race Game

import turtle
import random

dice = [1,2,3,4,5,6]

turtle.title("Turtle Race")
turtle.setup(width=800, height=600)

#Setup turtles

playerone = turtle.Turtle()
playerone.color('blue')
playerone.shape('turtle')
playerone.penup()
playerone.goto(-200,100)

#setup second turtle
playertwo = playerone.clone()
playertwo.color('red')
playertwo.penup()
playertwo.goto(-200,-100)

#turtles homes
#turtle one
playerone.goto(300,60)
playerone.down()
playerone.circle(40)
playerone.up()
playerone.goto(-200,100)

#turtle two
playertwo.goto(300,-140)
playertwo.down()
playertwo.circle(40)
playertwo.up()
playertwo.goto(-200,-100)

input('Pause - Get ready to RACE! - press Enter to start')

#Start of the game
for i in range (20):
    if playerone.pos() > (300,100):
        print ('Player One Wins')
        break
    elif playertwo.pos() >=(300,100):
        print ('Player two wins')
        break
    else:
        input('Player One press ENTER to roll the dice')
        outcome = random.choice(dice)
        playerone.fd(20*outcome)
        input('Player two press ENTER to roll the dice')
        outcome = random.choice(dice)
        playertwo.fd(20*outcome)


print ('Game Over')

    
