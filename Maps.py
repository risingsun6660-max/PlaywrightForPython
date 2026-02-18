#Map is a built in utility that applies a specified function to each item in an iterable
#returns a map object which is an iterator
#used to transform data without the use of explicit loops

#map(function,iterables)

numbers = [1,2,3,4,5,6,7]

squares = list(map(lambda x:x**2,numbers))
print(squares)
print(type(map(lambda x:x**2,numbers)))


#multiple iterables

num1 = [1,2,3]
num2 = [4,5,6]

multiply = list(map(lambda x,y:x*y,num1,num2))
print(multiply)