class Zoo(object):
    animals = set()
    def __init__(self, capacity):
        self.capacity = capacity 

    def getRemaindingSpace(self):
        return self.capacity

    def addAnimal(self, animal):
        self.capacity -= animal.getSpace
        Zoo.animals.add(animal)
        animal.zoo = self

class Animal(object):
    def __init__(self, name, space = 5, zoo = None):
        self.name = name 
        self.space = space 
        self.zoo = zoo 

    def getSpace(self):
        return self.space
    
    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, Animal) and self.name == other.name
    
    def __repr__(self):
        return 'Animal named ' + self.name 

    def __getZoo__(self):
        return self.zoo

class Bird(Animal):
    def __repr__(self):
        return "Bird names " + self.name 

    def __eq__(self, other):
        return isinstance(other, Bird) and self.name == other.name 

    def layEgg(self):
        newName = self.name + ' Jr'
        animal = Bird(newName, self.space)
        self.zoo.addAnimal(animal)

        

