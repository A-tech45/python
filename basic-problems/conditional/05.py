password = "hel" 
paswd = int(len(password))

if paswd >= 8 :
    print("strong passoword")
elif paswd < 8 and paswd >= 6 :
    print("weak passoword")
elif paswd < 6 and paswd >= 4:
    print("very weak passoword")

else:
    print("Your acc will be hacked");
