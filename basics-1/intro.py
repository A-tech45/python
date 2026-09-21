"""
OK LETS START FROM THE BASICS OF TERMINAL 
    
    1.WE CAN IMPORT OUR PYTHON FILE DIRECTLY IN OUR TERMINAL
        eg: if u have saved a file name hello.py in home/python/hello.py then u have to go inside that directory
        eg: cd home/python
        then in terminal import it using  import hello don't need to write .py here name is enough 
        -- Ok now we have learned to import files in terminal and work with them  

    2.We can call a function of a file from another file ( That's the thing i got new in python )
        Ok let me Explain  
            If u have  a function in hello.py 
                eg:>>> def op():
                    >>>    print("Welcome !!")

            We can call this in another file assume hi.py 
                 Lets learn how
                    Go to the hi.py file and import the op() function 
                        eg:>>> from hello import op()  
                           >>> op()      -- this will call the function defined in the hello.pyt

    3.We have already learned import now if u import a file and after that make changes in the original file then the 
    imported files doesnot have the changes saved . I mean we have to close the session and start again and import or 
    reload the file 

        So we will learn about reload 
            So reload is a method that we have to import from importlib  . Lets see how
                assume we have to reload the hello file 
                eg: >>> from importlib import reload
                    >>> reload(hello)                        

                Now hello will be reloaded and willl include the changes u made 

    4.U can call file variables(attributes)

        OK let see how 
            assume u have hello_p = "saktiman"
            then u can call this directly from terminal or another file
            -- From another file same as calling function first import then hello_p --

            From terminal import the file 
                then call it using filename.variable/attribute name
                    eg: hello.hello_p  -- Simple   
                            
                            
                            
"""

def op():
    print("Hello")

print("jekk");
oh = 2 + 2 