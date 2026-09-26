# count first non duplicate character
letter = "tootace"

for val in letter:
    if letter.count(val) == 1 :
        print(val)
        exit()