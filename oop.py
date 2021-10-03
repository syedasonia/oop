# allowing variables to the given parameter  
class car:
    def __init__(self, manufacturer, weight, colour, year):
	        self.manufacturer = manufacturer 
	        self.weight = weight
	        self.colour = colour
	        self.year = year 
# creating to instances for our class 
civic2007 = car ("Honda", "1276", "Light Blue" ,"2007")

qb2008  = car ("Honda", "1286", "Drack Blue" ,"2008")

#printing instances' variables 
print(civic2007.colour)