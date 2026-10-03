students = {
    101:{
       "name" : "akash",
       "roll" : 54 ,
       "mark" : 43
    }
}


def add_stu ( roll_no , mark , name ) :
  students[roll_no]={
        "name" : name ,
        "mark" : mark 
    }
    

name = input("ENtr name")
roll = int(input("ENtr roll no"))
mark = input("ENtr mark")
    
add_stu( roll , mark,name)
print(students)
   



