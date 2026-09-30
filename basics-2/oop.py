class car :
    def __init__ (self , model , brand):
        self.model = model
        self.brand = brand

mycar = car("toyota" , "harrier")

print(mycar.brand)
print(mycar.model)