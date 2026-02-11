#Dictionary is a collection of key value pairs where each key is unique and immutable

dict1 = {1:"john",2:"ben"}
print(dict1)
print(type(dict1))

print(dict1[1])
print(dict1[2])


dict2 ={"male":"john","female":"kate"} #keys also be string
print(dict2["male"])

#can also be a mixed 
dict3 ={"male":"john","female":"kate",2:["doremon","chingchan","sk"]}
print(dict3[2])
print(dict3.get("female"))

print(dict3.get("address"))#will return none
#print(dict3["address"])# will give error


#update a dictionary

dict4 = {1:"john",2:"kate"}
dict4[3]= "ben"
print(dict4)

#deleting dictionary
squares = {1:1,2:4,3:9,4:16,5:25}
print(squares)
squares.pop(4) # removes the key value 4:16
print(squares)
squares.popitem() #REMOVES THE LAST ITEM IN THE DICTIONARY
print(squares)
squares.clear() #REMOVES ALL THE KEY VALUES
print(squares)

squares1 = {1:1,2:4,3:9,4:16,5:25}
print(squares1)
del squares1
#print(squares1) #GIVES AN ERROR AS NAME IS NOT DEFINED AS ITS ALREADY DELETED


#MEMBERSHIP TEST IN DICTIONARY

squares2 = {1:1,2:4,3:9,4:16,5:25}
print(1 in squares2) # return true as 1 is present
print(45 in squares2)# return false as 1 is present
print(45 not in squares2) # return true as 45 is not present