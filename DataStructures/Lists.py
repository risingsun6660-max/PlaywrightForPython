list = [1,2,3,4]
print(list)
print(type(list))
print(len(list))

# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])

print(list[-1]) #prints the array from the end in the reverse
print(list[-2])
print(list[-3])
print(list[-4])


list1 = ["python","java","angular","spring"]
print(list1)
print(type(list1))


list2 = ["python",4,4.4,"java","spring"]
print(list2)
print(type(list2))

list2.append("go") # adds the value to the end of the list
print(list2)

list2.insert(0,"hello") # adds based on the index position
print(list2)


list2.pop() # removes last elemt of the array
list2.pop(1) #indexed location will be removed
print(list2)

list2.remove("java")# removes only first element in the list, if there are more values need to remove sepaerately
print(list2)

# max and min

li = [1,4,8,77,9,6]
print(max(li))
print(min(li))


#traverse through list using for loop
for i in li:
    print(i)



# Exercise to ask input frm the user and create a list out of that

noOfList = int(input("Enter total values in the list :- "))
print(noOfList)
i=1
listValue=[]
# while i<=noOfList:
#     print("Values are",i,noOfList)
#     listValue.append(input("Please enter the value to be added"))
#     i= i+1
# print(listValue)


#using for loop
for i in range(noOfList):  
    listValue.append(input("Please enter the value to be added"))
print(listValue)

