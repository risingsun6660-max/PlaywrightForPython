def function_name():
    pass

def sumOfNumbers(a,b):
    print(a+b)

sumOfNumbers(9,9)

def multply(a,b):
    result = a*b
    return result

print(multply(2,5))

def subtract(a,b=5):
    result = a-b
    return result

print(subtract(b=10,a=20))

#return max of 2 values

def max(a,b):
    if a>b:
        return a
    else:
        return b
    
print(max(2,5))


#exercise to take 3 numbers and return the biggest

def max(a,b,c):
    if a==b and a==c:
        print("all are equal")
    elif a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
print(max(3,1,7))


# the arguments passed as part of the function call are called actual arguements
# and the ones defined at function definition are formal arguements


#doc strings are string literals that comes right after the function,class,or method definition
#they provide clear description of what it does
#in the below the comment is the docstring, if you hover over the function name you can see the description within the comment

def wishes(name,wish):
    """
    this function greets the person with wishes
    """
    print("hello",name,wish)

wishes("john","Have a great day")


#types of arguments
#Positional arguments,Keyword arguements, arbitrary arguments

def greet(name,wish):
    print("hello",name,wish)

greet("john","Have a great day") # identifies based on the position hence called positional arguements

greet(wish="Have a great day",name="john")#keywords are given so position does not matter

# you can mix keyword and positional arguments but keyword should be the last one always
#greet(wish="Have a great day","john") # give an error as positional argument is coming after keyword

#arbitrary arguments are used when we dont know how many arguments are passed to the function
def greet(*names):
    for name in names:
        print("hello",name)
greet("john","ben","kim","pino","bob")