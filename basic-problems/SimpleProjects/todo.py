todo = [ ]
print("1.Add items \n2.Delete items")
def todoo() :
    choice = int(input("Enter ur choice :"))
    match choice:
     case 1:
        value1 = input("What u want to add")
        todo.append(value1)
        print(todo)
        todoo()
     case 2:
        print("Removing elements ....")
        todo.pop()     # we can use .remove() function here to remove the user wanted element 
        print(todo)
        todoo()
     case _: print("Invalid input")
todoo()
