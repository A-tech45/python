# Basic car class
class car :
    total = 0
    def __init__ (self , model , brand):
        self.model = model
        self.__brand = brand
        car.total += 1 

    def fullname(self):
        return f"{self.__brand} {self.model}"

    # To make a static method we have to use decorators
    @staticmethod
    def ststicmethod():
         return "This is a static Method"

    def g_brand(self):
        return self.__brand + " This is private now and is called inside the class "

# This method is in bith the class but return different results ( this is polymorphism)
    def fuel_type(self) :
        return "petrol or disel"

class Electric(car) :
    def __init__(self , model , brand , battery):
        super().__init__(brand , model)  # used to inherit from the previous class 
        self.battery = battery

# This method is in bith the class but return different results ( this is polymorphism)
    def fuel_type(self) :
            return "electric"


        
mycar = Electric("toyota" , "harrier", "75kWh")
mycr = car("toyota" , "harrier")
mycr = car("toyota" , "sonnet")

#Check if mycar is an instance of the class car // returns true or false boolean value
#print(isinstance(mycar , car))

#print(mycar.__brand) # u cannot call the brand directly as i has become private  
#print(mycar.fullname())  # here u can call becuase fullname is a method of that class itself so its calling inside that class 
#print(mycar.fuel_type()) 
#print(mycr.fuel_type()) 
#print(car.total)
#print(mycar)


class battery :
     def engine_info(self) :
          return "This is a engine"

class engine :
     def batttery_info(self):
          return "This is a battery"

class electric_car_2(battery , engine , car) :  # Here electriccar2 inherit from class engine , battery and car 
     pass



caaar = electric_car_2("Ghopghop" ,"tesla")
print(caaar.batttery_info())
print(caaar.engine_info())