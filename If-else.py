a=3
if a>4:
    print("a is greater than 4")#indentation(4 spaces or 1 tab) tells that this is inside the if condition
print("a is not greater than 4")

if a>=3:
    print("a is greater than or equal to 3")
else:
    print("a is not greater than or equal to 3")


k=1
l=0

if k: #returns true if 1 or more than 1
    print("yes")
else:
    print("no")


if l: #return false if 0
    print("yes")

else:
    print("no")

if k and l:
    print("yes")
else:
    print("no")

if k or l:
    print("yes")
else:
    print("no")



#program to take the favorite cartoon as input and check if its doremon

character = input("Enter your favourite cartoon charactes:- ")
if character == "Doremon":
    print("I love this show too")
else:
    print("Good choice. But I like a different one")



#elif

myMarks = 70

if myMarks>=90:
    print("Your garde is A+")
elif myMarks>=80:
    print("Your garde is A")
elif myMarks>=70:  
    print("Your garde is B")
else:
    print("You nee dto focus, grade is C")