# lecture of inheritance 
#resturant manu 



class drink:
    def __init__(self, name, price, flavors ,ingredients):
        self.name =name
        self.price = price
        self.flavors = flavors
        self.ingredients = ingredients
    
class starters:
        def __init__(self, name, price, catagories ,ingredients):
            self.name =name
            self.price = price
            self.catagories = catagories
            self.ingredients = ingredients   
            

class mainmenu:
    def __init__(self, name, price, catagories ,ingredients):
            self.name =name
            self.price = price
            self.catagories = catagories
            self.ingredients = ingredients   
            
        

 
class dessert:
    def __init__(self, name, price, catagories ,ingredients):
            self.name =name
            self.price = price
            self.catagories = catagories
            self.ingredients = ingredients   
            
       
food1 = drink("coke","£2","No-suger","Non-Alcoholic")
food2 = starters("Dimsum","£10","chinese","chicken")
food3 = mainmenu("cuisines","£15","indian","lam")
food4 = dessert("pie","£1","english","egg")

print(food1.price)
print(food2.name)
print(food3.catagories)
print(food4.name,food4.price , food4.catagories ,food4.ingredients)
