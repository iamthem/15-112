# Leandro Lopez
# lslopez
# Section H 
#################################################
# Hw9
#
# No iteration! no 'for' or 'while'.  Also, no 'zip' or 'join'.
# You may add optional parameters
# You may use wrapper functions
#################################################

import cs112_f17_week9_linter

def almostEqual(x, y, epsilon = 10**-8):
    return abs(x-y) < epsilon

##############################################
# Recursive questions
##############################################

# Find power sum 
def powerSum(n, k):
    if n <= 0: #Base case and negatives check 
        return 0
    elif k < 0: #Make sure exponent is positive 
        return 0 
    else: 
        return n**k + powerSum(n-1,k) #Multiply current step and add next step 

def sumOfSquaresOfDigits(n):
    if n == 0: # Base case 
        return 0
    else:
        #square current digit and add the square of the next one 
        return (n%10)**2 + sumOfSquaresOfDigits(n//10) 

def isHappyNumber(n):
    if n < 1: return False # Negatives and zero are sad 
    elif n == 4: return False # Four is sad 
    else:
        n = sumOfSquaresOfDigits(n) #Find sum of digits and assign it to n
        if n == 1: return True # One is happy 
        else: return isHappyNumber(n) # Try again with new n 



def evalPrefixNotation(L):
    return 42

##############################################
# OOP questions
##############################################

class VendingMachine(object):

    def __init__(self, bottles, price): #Initialize variables 
        self.bottles = bottles
        self.price = price
        self.staticPrice = price #Static price to keep track of initial price
        if bottles > 0: #Status of the vending machine  
            self.empty = False 
        else: self.empty = True 
    
    def __str__(self): #Printing format
        #Several bottles, nonzero paid, noninteger number of dollars
        if (self.staticPrice-self.price != 0 and self.bottles != 1
                and (self.staticPrice/100 != int(self.staticPrice/100))):
            return "Vending Machine:<%d bottles; $%4.2f each; $%4.2f paid>" % \
                (self.bottles, self.staticPrice/100, 
                        (self.staticPrice-self.price)/100)
        #1 bottle, nonzero paid, noninteger number of dollars
        elif (self.staticPrice-self.price != 0 and self.bottles == 1
                and (self.staticPrice/100 != int(self.staticPrice/100))):
            return "Vending Machine:<%d bottle; $%4.2f each; $%4.2f paid>" % \
                (self.bottles, self.staticPrice/100, 
                        (self.staticPrice-self.price)/100)
        # Several bottles, zero paid, noninteger number of dollars
        elif (self.staticPrice-self.price == 0 and self.bottles != 1 and
                (self.staticPrice/100 != int(self.staticPrice/100))):
            return "Vending Machine:<%d bottles; $%4.2f each; $0 paid>" % \
                        (self.bottles, self.staticPrice/100)
        # 1 bottle, zero paid, noninteger number of dollars
        elif (self.staticPrice-self.price == 0 and self.bottles == 1 and
                (self.staticPrice/100 != int(self.staticPrice/100))):
            return "Vending Machine:<%d bottle; $%4.2f each; $0 paid>" % \
                        (self.bottles, self.staticPrice/100)
        # 1 bottle, zero paid, integer number of dollars
        elif (self.staticPrice-self.price == 0 and self.bottles == 1 and 
                (self.staticPrice/100 == int(self.staticPrice/100))):
            return "Vending Machine:<%d bottle; $%d each; $0 paid>"%\
                (self.bottles, int(self.staticPrice/100))
                
    def __eq__(self, other): #Test for equality 
       return (isinstance(other, VendingMachine) and (self.bottles == 
           other.bottles) and (self.price == other.price)) 

    def getHashables(self): #get hashable parameters 
        return (self.bottles, self.price)

    def __hash__(self): #apply hash function on hashable parameters
        return hash(self.getHashables())

    def isEmpty(self): #Check if vending machine is empty 
        if self.bottles == 0: 
            self.empty = True  
            return self.empty
        if self.bottles > 0:
            self.empty = False 
            return self.empty

    def getBottleCount(self): # Get number of bottles 
        return self.bottles 

    def stillOwe(self): # Get current price 
        return self.price

    def insertMoney(self, money): #Insert money 
        if not self.empty: #If vending machine is not empty accept money  
            self.price -= money #deduct money received from price 
            if self.price == 0: #Dispense bottle 
                self.price = self.staticPrice  
                self.bottles -= 1 #Subtract dispensed bottle 
                return ("Got a bottle!", 0)
            #Check to see if printing cents is necessary 
            elif self.price/100 == int(self.price/100):
                return ("Still owe $%d" % (int(self.price/100)), 0)
            elif self.price > 0: #Print cents  
                return ("Still owe $%4.2f" % (self.price/100), 0)
            else: #Gave vending machine extra money 
                change = self.price * -1
                self.price = self.staticPrice 
                self.bottles -= 1
                return ("Got a bottle!", change) #Return change 
        else: return ("Machine is empty", money) #machine is empty return money

    def stockMachine(self, bottles): #Restock machine
        self.bottles += bottles
    
#################################################
# Test Functions
#################################################

def testPowerSum():
    print('Testing powerSum()...', end='')
    assert(powerSum(4, 6) == 1**6 + 2**6 + 3**6 + 4**6)
    assert(powerSum(0, 6) == 0)
    assert(powerSum(4, 0) == 1**0 + 2**0 + 3**0 + 4**0)
    assert(powerSum(4, -1) == 0)
    print('Done!')

def testIsHappyNumber():
    print('Testing isHappyNumber()...', end='')
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print('Done!')

def testEvalPrefixNotation():
    print('Testing evalPrefixNotation()...', end='')
    assert(evalPrefixNotation([42]) == 42)
    assert(evalPrefixNotation(['+', 3, 4]) == 7)
    assert(evalPrefixNotation(['-', 3, 4]) == -1)
    assert(evalPrefixNotation(['-', 4, 3]) == 1)
    assert(evalPrefixNotation(['+', 3, '*', 4, 5]) == 23)
    assert(evalPrefixNotation(['+', '*', 2, 3, '*', 4, 5]) == 26)
    assert(evalPrefixNotation(['*', '+', 2, 3, '+', 4, 5]) == 45)
    assert(evalPrefixNotation(['*', '+', 2, '*', 3, '-', 8, 7,
                               '+', '*', 2, 2, 5]) == 45)
    print('Done!')

def testVendingMachineClass():
    print("Testing Vending Machine class...", end="")
    # Vending machines have three main properties: 
    # how many bottles they contain, the price of a bottle, and
    # how much money has been paid. A new vending machine starts with no
    # money paid.
    vm1 = VendingMachine(100, 125)
    assert(str(vm1) == "Vending Machine:<100 bottles; $1.25 each; $0 paid>")
    assert(vm1.isEmpty() == False)
    assert(vm1.getBottleCount() == 100)
    assert(vm1.stillOwe() == 125)
    
    # When the user inserts money, the machine returns a message about their
    # status and any change they need as a tuple.
    assert(vm1.insertMoney(20) == ("Still owe $1.05", 0))
    assert(vm1.stillOwe() == 105)
    assert(vm1.getBottleCount() == 100)
    assert(vm1.insertMoney(5) == ("Still owe $1", 0))
    
    # When the user has paid enough money, they get a bottle and 
    # the money owed resets.
    assert(vm1.insertMoney(100) == ("Got a bottle!", 0))
    assert(vm1.getBottleCount() == 99)
    assert(vm1.stillOwe() == 125)
    assert(str(vm1) == "Vending Machine:<99 bottles; $1.25 each; $0 paid>")
    
    # If the user pays too much money, they get their change back with the
    # bottle.
    assert(vm1.insertMoney(500) == ("Got a bottle!", 375))
    assert(vm1.getBottleCount() == 98)
    assert(vm1.stillOwe() == 125)
    
    # Machines can become empty
    vm2 = VendingMachine(1, 120)
    assert(str(vm2) == "Vending Machine:<1 bottle; $1.20 each; $0 paid>")
    assert(vm2.isEmpty() == False)
    assert(vm2.insertMoney(120) == ("Got a bottle!", 0))
    assert(vm2.getBottleCount() == 0)
    assert(vm2.isEmpty() == True)
    
    # Once a machine is empty, it should not accept money until it is restocked.
    assert(str(vm2) == "Vending Machine:<0 bottles; $1.20 each; $0 paid>")
    assert(vm2.insertMoney(25) == ("Machine is empty", 25))
    assert(vm2.insertMoney(120) == ("Machine is empty", 120))
    assert(vm2.stillOwe() == 120)
    vm2.stockMachine(20) # Does not return anything
    assert(vm2.getBottleCount() == 20)
    assert(vm2.isEmpty() == False)
    assert(str(vm2) == "Vending Machine:<20 bottles; $1.20 each; $0 paid>")
    assert(vm2.insertMoney(25) == ("Still owe $0.95", 0))
    assert(vm2.stillOwe() == 95)
    vm2.stockMachine(20)
    assert(vm2.getBottleCount() == 40)
    
    # We should be able to test machines for basic functionality
    vm3 = VendingMachine(50, 100)
    vm4 = VendingMachine(50, 100)
    vm5 = VendingMachine(20, 100)
    vm6 = VendingMachine(50, 200)
    vm7 = "Vending Machine"
    assert(vm3 == vm4)
    assert(vm3 != vm5)
    assert(vm3 != vm6)
    assert(vm3 != vm7) # should not crash!
    s = set()
    assert(vm3 not in s)
    s.add(vm4)
    assert(vm3 in s)
    s.remove(vm4)
    assert(vm3 not in s)
    assert(vm4.insertMoney(50) == ("Still owe $0.50", 0))
    assert(vm3 != vm4)
    print("Done!")

##############################################
# testAll and main
##############################################

def testAll():
    testPowerSum()
    testIsHappyNumber()
    testEvalPrefixNotation()
    testVendingMachineClass()

def main():
    cs112_f17_week9_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
