"""
Fun with Graphics
Fernando Branco
CIS129
"""

from turtle import*

#Draw dot
dot(25,"red")
pu()
setpos(12,0)
pencolor("blue")

#move cursor
down()

#move forward
fd(100)
pu()
setpos(100,0)
dot(50,"yellow")

#Change direction
rt(180)
down()

#Change pen width
pensize(6)
fd(100)

#Draw Circle
circle(35)
pu()

#Set home
home()
setpos(0,35)
speed(1)
down()
circle(35)
