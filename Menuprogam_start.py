#Menu Program

def numberofscoops():
    global scoops
    global costofscoop
    print('Pick number of scoops')
    print('---------------------')
    print('1.One Scoop')
    print('2.Two Scoops')
    print('3.Three Scoops')
    print('')
    numscoops = int(input('How many scoops?:'))
    if numscoops ==1:
        costofscoop = 2.2
        scoops = "One Scoop"
    elif numscoops == 2:
        costofscoop = 3.0
        scoops = 'Two Scoops'
    else:
        costofscoop =4.0
        scoops = 'Three Scoops'

def pickflavors():
    global flavor
    print('')
    print('Pick flavors')
    print('---------------------')
    print('1.Strawberry')
    print('2.Chocolate')
    print('3.Vanila')
    print('')
    theflavor = int(input('Pick your Flavor?:'))
    if theflavor == 1:
        flavor = "Strawberry"
    elif theflavor == 2:
        flavor = 'Chocolate'
    else:
        flavor = 'Vanila'

def addons():
    global theaddon
    global costofaddon
    print('')
    print('Pick additional toppings')
    print('---------------------')
    print('1.Nuts')
    print('2.Hot Fudge')
    print('3.Caramel')
    print('')
    choice = int(input('Pick Topping?:'))
    if choice ==1:
        theaddon = 'Nuts'
    elif choice ==2:
        theaddon = 'Hot Fudge'
    else:
        theaddon = 'Caramel'
    costofaddon = 0.50            

    

def menu():
    print("")
    print("What do you want to do")
    print("**********************")
    print("1. Pick Number Of Scoops")
    print("2. Choose Ice Cream Flavor")
    print("3. Pick Additional topping")
    print("7. Quit the program")
    print("")
    print("Please press the number of your choice...")
    print("")
    print("(7 will exit the program)")
    print("")
    return int(input("What is your Selection?  "))

# Function to convert number into string 
# Switcher is dictionary data type here 
def numbers_to_strings(argument): 
    switcher = { 
        1: "numberofscoops", 
        2: "pickflavors",
        3: "addons"
    } 
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return switcher.get(argument, "nothing") 

#MAIN
argument=0
costofscoop = 0.0
costofaddon = 0.0
scoops = ""
flavor = ""
theaddon = ""

while argument != 7:
 
    argument=menu()
    if argument == 7: break
    methodcall = numbers_to_strings(argument)
    #print(argument)
    #print(numbers_to_strings(argument) )
    print("You picked: ", methodcall)
    locals()[methodcall]()

#Print Options
print('Review your order')
print('You Picked: ', scoops)
print('Your Flavor: ', flavor)
print('You Added: ',theaddon)
totalcost = costofscoop + costofaddon
print('Your total is $%.2f'%totalcost)


print('Program Ended')

 
