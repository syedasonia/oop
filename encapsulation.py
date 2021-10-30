# example of encapsulation 
"""
class CheddarMultiflvourpack():
    def __init__(self,flavour,weight):
        self.flavour = flavour
        self.weight = weight
    
    def display(self):
        print(self.flavour)
        print(self.weight)

cheddarcatagorione = CheddarMultiflvourpack('BBQ', 15) 
cheddarcatagoritwo = CheddarMultiflvourpack('chilli', 15)
cheddarcatagorithree = CheddarMultiflvourpack('original', 15)
#accessing using class method
cheddarcatagorione.display() 
cheddarcatagoritwo.display()
#accessing directly from outside
print(cheddarcatagorione.flavour,cheddarcatagorione.weight)  
print(cheddarcatagoritwo.flavour,cheddarcatagoritwo.weight) 
print(cheddarcatagorithree.flavour,cheddarcatagorithree.weight)    
"""
# a simple class with some attibutes and it's instances

class CheddarMultiflvourpack():
    def __init__(self,flavour,weight):
        self.flavour = flavour
        self.weight = weight

    def display(self):
          print(self.flavour)
          print(self.weight)

class Cheddarcatagoritwo(CheddarMultiflvourpack): 
    def __init__(self, flavour, weight):
        super().__init__(flavour, weight)  

class Cheddarcatagorithree(CheddarMultiflvourpack):
    def __init__(self, __flavour, __weight):
        super().__init__(__flavour, __weight)  

    def dontdisplay(self):
          print(self.__flavour)
          print(self.__weight)
    

cheddarcatagorione = CheddarMultiflvourpack('BBQ', 15)
cheddarcatagoritwo = Cheddarcatagoritwo('chilli', 15) 
cheddarcatagorithree = Cheddarcatagorithree('original', 15)
#accessing using class method

cheddarcatagorione.display()
cheddarcatagoritwo.display()
cheddarcatagorithree.dontdisplay()

#accessing directly from outside
print(cheddarcatagorione.flavour,cheddarcatagorione.weight) 
print(cheddarcatagoritwo.flavour,cheddarcatagoritwo.weight) 
print(cheddarcatagorithree.__flavour,cheddarcatagorithree.__weight)