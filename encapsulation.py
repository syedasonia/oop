# example of encapsulation 


# a simple class with some attibutes and it's instances

class CheddarMultiflvourpack():
    def __init__(self,flavour,weight):
        self.flavour = flavour
        self.weight = weight
    
    def display(self):
        print(self.flavour)
        print(self.weight)

cheddarcatagorione = CheddarMultiflvourpack('BBQ', 15) 
cheddarcatagoritwo = CheddarMultiflvourpack('chilli', 15)
#accessing using class method
cheddarcatagorione.display() 
cheddarcatagoritwo.display()
#accessing directly from outside
print(cheddarcatagorione.flavour,cheddarcatagorione.weight)  
print(cheddarcatagoritwo.flavour,cheddarcatagoritwo.weight)    