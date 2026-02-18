# Filters are used to extract elements from an iterable(like list,set,tuple) that satisfy given condotion
#returns a filter object which can be converted to list,tuple
#filter(function,iterable)

def isOdd(num):
    if num%2 != 0:
        return True
    return False

numlist = [1,2,3,4,5,6,7,8,9]

isodd = list(filter(isOdd,numlist))

#print(isodd)


#the above using lambda function

isOddLambda = list(filter(lambda x:x%2!=0,numlist))
print(isOddLambda)


#filter words with more than 5 letters

words = ["apple","banana","kiwi","strawberry"]

wordsMoreThanFive = list(filter(lambda w:len(w)>5,words))

print(wordsMoreThanFive)


#filtering falsy values such as None,0,empty strings

words1 = ["apple",None,"banana",0,"strawberry",""]
filterFlasyValues = list(filter(None,words1))
print(filterFlasyValues)