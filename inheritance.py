# lecture of inheritance 
#resturant manu 

class restaurantmenu:
    def __init__(self,name, price,ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients   
class menucatagories(restaurantmenu):
    def __init__(self, name, price, catagories,ingredients):
        super().__init__(name, price,ingredients)
        self.catagories= catagories

class drink(restaurantmenu):
    def __init__(self, name, price, flavors ,ingredients):
        super().__init__(name, price,ingredients)
        self.flavors = flavors
    
class starters(menucatagories):
        def __init__(self, name, price, catagories ,ingredients):
            super().__init__(name, price, catagories ,ingredients)
            

class mainmenu(menucatagories):
    def __init__(self, name, price, catagories ,ingredients):
        super().__init__(name, price, catagories ,ingredients)
        

 
class dessert(menucatagories):
    def __init__(self, name, price, catagories ,ingredients):
        super().__init__(name, price, catagories ,ingredients)
       
food1 = drink("coke","£2","No-suger","Non-Alcoholic")
food2 = starters("Dimsum","£10","chinese","chicken")
food3 = mainmenu("cuisines","£15","indian","lam")
food4 = dessert("pie","£1","english","egg")

print(food1.price)
print(food2.name)
print(food3.catagories)
print(food4.name,food4.price , food4.catagories ,food4.ingredients)
