#Lambdas are small anonymous functions
#Can have multiple arguements but only single expression
#Often used for short, throwaway functions(functions that are defimed and used in the same scope)
#syntax lambda arguements:expression
double = lambda x:x*2

print(double(50))

divide = lambda x,y:x/y

print(divide(10,2))


#lambda function inside a function
def func_anon(a):
    return lambda b:b-a

print(func_anon(5)(2))
#can also be written as below
var_lambda = func_anon(5)
print(var_lambda(2))