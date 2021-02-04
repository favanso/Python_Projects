'''
M10 Assignment
Automobile Class
Fernando Branco
CIS129
Created 04-14-2020
'''

class automobileloan:
    def __init__(self):
        self.LoanID = "123ABC"
        self.CarMake = ""
        self.CarModel = 99
        self.LoanBalance = 0.0
        
#Setters
        
    def setLoanID(self,var1):
        self.LoanID = var1
        
    def setCarMake(self,var1):
        self.CarMake = var1
        
    def setCarModel(self,var1):
        self.CarModel = var1
        
    def setLoanBalance(self,var1):
        self.LoanBalance = var1

#Getters

    def getLoanID(self):
        return self.LoanID

    def getCarMake(self):
        return self.CarMake

    def getCarModel(self):
        return self.CarModel

    def getLoanBalance(self):
        return self.LoanBalance
        
    
    #Utility Methods
    def displayvalues(self):
        print ("Loan ID = ",self.LoanID)
        print ('Car Make = ',self.CarMake)
        print ('Car Model = ',self.CarModel)
        print('Loan Balance = ',self.LoanBalance)

    def displaybalance(self):
        print('The Loan Balance is ',self.LoanBalance)


#Main
carloan = automobileloan()
carloan.displayvalues()

#send data to setters
carloan.setLoanID("FGB123GV")
carloan.setCarMake("AUDI")
carloan.setCarModel (899)
carloan.setLoanBalance(80000)
carloan.displayvalues()
#Getters
print ("The loan ID is: ", carloan.getLoanID())
carloan.displaybalance()
