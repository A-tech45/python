"""
Ok there is a concept in python that is very different from others 
    in python every variable we create it creates an object from it 
        eg: x = 10 than an object of x is created in the memory that cannot be changes / but can be replaced 
            I mean if we say x = 20 then x will point to 20 (where 20 is the newly created object but 10 remains as it is )
    ok lets understand by a programme 
"""

x  = 10 ;
y = x  

x = 19 ;
print(y) 

""" Ok here y will print 10 becuase its pointing to 10 
        Here the doubts comes , but y = x
          let me explain 
            when we declare x = 10 it creates a object 10 in the memory (so x is pointing to 10)
            y = x Here the concept is y is not pointing to x . y is pointing to the same object that 
                   x was pointing to That is 10
                   So when we changed x = 15 , now x is pointing to new object 15 but 10 is still there 
                   and we have not changed y value so y is pointing to 10  
     
      
"""