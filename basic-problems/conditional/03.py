# U can use input i am making just shorter
score = 43
#grade = ""

if score >=100 :
    print("Invalid Mark !!")
    exit()
if score >= 90 :
    grade = "A" ;
elif score < 90 and score >= 80 :
    grade  = "B" ;
elif score < 80 and score >= 70 :
    grade = "C"
elif score < 70 and score >= 60 :
    grade  = "D"
elif score < 60 and score >= 50 :
    grade = "E"
else :
    grade = "F"

print(grade)