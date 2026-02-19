#Recursio is calling the function again and again

def fact(x):
    if x==1:
        return 1
    else:
        return (x*fact(x-1))

num = 4
print(fact(num))
    