a=2

if a<10:
    if a>3:
        print("a is greater than 3 and less that 10")
    else:
        print("a is less than 3")

else:
    print("a is greater than 10")


# /excercise
# check if age greater than 18 then he can drive a car, or greter than 16 and less tha 18 then bike,cycle

age = int(input("Enter the age:- "))
if age>=16:
    if age>=18:
        print("He can drive a FOur wheeler")
    else:
        print("He can drive a two wheeler vehicle")
else:
    print("Under Age")
