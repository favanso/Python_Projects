##Create the PYTHON program allowing the user to enter a value for one edge of a cube(A box-shaped solid object that has six identical square faces).
##
##Prompt the user for the value. 
##There should be a function created for each calculation:
##One function should calculate the surface area of one side of the cube. The value calculated is printed within the function.
##One function should calculate the surface area of the whole cube.
##The user value is passed as an argument to this function. It should  be returned to the calling statement and printed.
##One function should calculate the volume of the cube and print the results within in the function.

'''
Fernando Branco
CIS 129
M9 Assignment
'''

value = float(input('Enter a value for one edge of a cube: '))

def oneside():
    os = value*value
    print ('The area of each cube side is ', os,'\n')
    print ('The side lenght you inputed is ',value,'\n')

def surfacearea(value):
    surf = value*6
    return surf

result = surfacearea(value)
print ('The Surface area of the cube is ', result,'\n')


def volume():
    vol = value**3
    print ('The volume of the cube is ', vol,'\n')


oneside()
volume()

