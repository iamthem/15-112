# Leandro Lopez
# lslopez
# Section H
# HW 11

import cs112_f17_week11_linter
import types

###################
# Problems
###################

class Gate(object):

    def __init__(self): #Initialize variables
        self.input1 = False
        self.input2 = False
        if type(self) != NotGate: #If objects aren't not gates set ins to 2
            self.inputs = 2
        else: self.inputs = 1 #If object is not gate, only one input
        self.output = 0

    def __str__(self): #Printing format
        #If object is not 'NotGate' return both inputs
        if not (type(self) == NotGate):
            return "%s(%r,%r)" % (type(self).__name__[:-4], self.input1,
                               self.input2)
        #If object is 'NotGate' return only first input
        else: return "%s(%r)" % (type(self).__name__[:-4], self.input1)

    # Return number of inputs
    def numberOfInputs(self):
        return self.inputs

    # Change inputs to a boolean
    def setInput(self, number, boolean):
        if number == 0:
            self.input1 = boolean
        elif number == 1:
            self.input2 = boolean

class AndGate(Gate):
    # For 'AND' to be true, both inputs must be true
    def getOutput(self):
        return self.input1 and self.input2

class OrGate(Gate):
    # For 'OR' gate to be true, one input must be true
    def getOutput(self):
        return self.input1 or self.input2

class NotGate(Gate):
    # For a not gate to be true, the unique input must be false
    def getOutput(self):
        return not self.input1
    # Return number of inputs (1 in case of NotGates)
    def numberOfInputs(self):
        return self.inputs

class ComplexNumber(object):
    zero = None #Initialize zero to None initially

    def __init__(self, real=0, imaginary=0): #Initialize variables
        if type(real) == int: #If complex object is given
            self.real = real
            self.imaginary = imaginary
        else: # If real and imaginary numbers are given
            self.real = real.real
            self.imaginary = real.imaginary

    def __str__(self): #Printing format
        return "%d+%di" % (self.real, self.imaginary)

    def __eq__(self, other): #Test for equality
        if type(other) == ComplexNumber:
            return (self.real == other.real and
                    self.imaginary == other.imaginary)
        else:
            return (self.imaginary == 0 and self.real == other)

    def getHashables(self): #get hashable parameters
        return (self.real, self.imaginary)

    def __hash__(self): #apply hash function on hashable parameters
        return hash(self.getHashables())

    def realPart(self): #Return real part
        return self.real

    def imaginaryPart(self): #Return imaginary part
        return self.imaginary

    @staticmethod #This method is static since it doesn't have self as param
    def getZero():
        if not ComplexNumber.zero: #If zero is not None
            # Make an instance of zero
            ComplexNumber.zero = ComplexNumber(0,0)
        return ComplexNumber.zero


#################
# Test Functions
#################

def getLocalMethods(clss):
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class.
    result = [ ]
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)

def testGateClasses():
    print("Testing Gate Classes... ", end="")

    # require methods be written in appropriate classes
    assert(getLocalMethods(Gate) == ['__init__', '__str__',
                                     'numberOfInputs', 'setInput'])
    assert(getLocalMethods(AndGate) == ['getOutput'])
    assert(getLocalMethods(OrGate) == ['getOutput'])
    assert(getLocalMethods(NotGate) == ['getOutput', 'numberOfInputs'])

    # make a simple And gate
    and1 = AndGate()
    assert(type(and1) == AndGate)
    assert(isinstance(and1, Gate) == True)
    assert(and1.numberOfInputs() == 2)
    and1.setInput(0, True)
    and1.setInput(1, False)
    # Hint: to get the name of the class given an object obj,
    # you can do this:  type(obj).__name__
    # You might do this in the Gate.__str__ method...
    assert(str(and1) == "And(True,False)")
    assert(and1.getOutput() == False)
    and1.setInput(1, True) # now both inputs are True
    assert(and1.getOutput() == True)
    assert(str(and1) == "And(True,True)")

    # make a simple Or gate
    or1 = OrGate()
    assert(type(or1) == OrGate)
    assert(isinstance(or1, Gate) == True)
    assert(or1.numberOfInputs() == 2)
    or1.setInput(0, False)
    or1.setInput(1, False)
    assert(or1.getOutput() == False)
    assert(str(or1) == "Or(False,False)")
    or1.setInput(1, True)
    assert(or1.getOutput() == True)
    assert(str(or1) == "Or(False,True)")

    # make a simple Not gate
    not1 = NotGate()
    assert(type(not1) == NotGate)
    assert(isinstance(not1, Gate) == True)
    assert(not1.numberOfInputs() == 1)
    not1.setInput(0, False)
    assert(not1.getOutput() == True)
    assert(str(not1) == "Not(False)")
    not1.setInput(0, True)
    assert(not1.getOutput() == False)
    assert(str(not1) == "Not(True)")

    print("Passed!")

def testComplexNumberClass():
    print("Testing ComplexNumber class... ", end="")
    # Do not use the builtin complex numbers in Python!
    # Only use integers!

    c1 = ComplexNumber(1, 2)
    assert(str(c1) == "1+2i")
    assert(c1.realPart() == 1)
    assert(c1.imaginaryPart() == 2)

    c2 = ComplexNumber(3)
    assert(str(c2) == "3+0i") # default imaginary part is 0
    assert(c2.realPart() == 3)
    assert(c2.imaginaryPart() == 0)

    c3 = ComplexNumber()
    assert(str(c3) == "0+0i") # default real part is also 0
    assert(c3.realPart() == 0)
    assert(c3.imaginaryPart() == 0)

    # Here we see that the constructor for a ComplexNumber
    # can take another ComplexNumber, which it duplicates
    c4 = ComplexNumber(c1)
    assert(str(c4) == "1+2i")
    assert(c4.realPart() == 1)
    assert(c4.imaginaryPart() == 2)

    assert((c1 == c4) == True)
    assert((c1 == c2) == False)
    assert((c1 == "Yikes!") == False) # don't crash here
    assert((c2 == 3) == True)

    s = set()
    assert(c1 not in s)
    s.add(c1)
    assert(c1 in s)
    assert(c4 in s)
    assert(c2 not in s)

    assert(ComplexNumber.getZero() == 0)
    assert(isinstance(ComplexNumber.getZero(), ComplexNumber))
    assert(ComplexNumber.getZero() == ComplexNumber())
    # This next one is the tricky part -- there should be one and
    # only one instance of ComplexNumber that is ever returned
    # every time you call ComplexNumber.getZero():
    assert(ComplexNumber.getZero() is ComplexNumber.getZero())
    # Hint: you might want to store the singleton instance
    # of the zero in a class attribute (which you should
    # initialize to None in the class definition, and then
    # update the first time you call getZero()).

    print("Passed!")


def testAll():
    testGateClasses()
    testComplexNumberClass()

def main():
    cs112_f17_week11_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
