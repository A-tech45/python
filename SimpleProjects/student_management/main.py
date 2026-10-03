# The demo data
import sys

student = {
    1: {"name": "Mohan mishra", "mark": "43"},
    2: {"name": "Rohan mishra", "mark": "23"},
}


def add_students(roll_no, name, mark):
    student[roll_no] = {"name": name, "mark": mark}


def remove_students(roll_no):
    del student[roll_no]


def update_mark(roll_no, mark):
    student[roll_no] = {"mark": mark}


while True :
    choice = int(input("Enter ur "))
    match choice:
        case 1:
            rollNo = int(input("Enter the roll no :"))
            name = input("Enter the name :")
            mark = int(input("Enter the mark :"))
            add_students(rollNo, name, mark)

        case 2:
            rollNo = int(input("Enter the roll no :"))
            remove_students(rollNo)

        case 3:
            rollNo = int(input("Enter the roll no :"))
            mark = int(input("Enter the mark :"))
            update_mark(rollNo, mark)

        case 4 :
            print(student)

        case 5:
            print("Exiting....")
            sys.exit()
