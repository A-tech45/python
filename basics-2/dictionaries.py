dic = {"price" : "999" , "name":"apache" , "model" : "latest"} ;
#print(dic[0])

print(dic.get("price"))

dic["model"] = "old" ;

print(dic)

for val in dic :
    print(val ,dic[val]) 

# prints the key and value in a dictionary only availiable in dictionary
for key , value in dic.items() :  
    print(key , value)

# u have to give string here or it will give an error
if "price" in dic :  
    print("yes") 

# gives the length of the dictionary 3 becuase there are three keys and values
print(len(dic))  

dic["engine"] = "v8"

# deletes the key value pair
dic.pop("price")

#deletes the last element  
dic.popitem() 

#deletes the entered value
del dic["name"] 
print(dic)

#The copy function is also applicable here
mdic = dic.copy()

#There can be nested dictionaries
chai_shop = {
    "chai" : {
        "masala":"good" ,
        "lemon":"decent",
        "ginger":"better"
    } ,
    "samosa" : {
        "aloo" : "fav" ,
        "paneer" : "excellent",
        "chicken" : "outstanding"
    }
}

#For acessing multiple nested dictionaries using .get method
print(chai_shop.get("chai").get("lemon")) 

#Usinf square method
print(chai_shop["chai"]["ginger"])