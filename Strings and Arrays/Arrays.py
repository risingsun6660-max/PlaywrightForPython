from array import *

# my_array = array(typecodes,initializers)

my_array = array('i',[1,2,3,4,5,6,7,8]) #cannot add float types in this array as its defined as integer

for x in my_array:
    print(x)

my_array1 = array('f',[1,2,3,4,5,6,7,8])
for x in my_array1:
    print(x)

# accessing the array
print(my_array1[4])

#adding to array
my_array1.insert(8,9.0)
print(my_array1)

#deleting 
my_array.remove(5) #return error if element is not present
print(my_array)

#search an element
print(my_array.index(7))


#update element
my_array[5] = 8
print(my_array)

