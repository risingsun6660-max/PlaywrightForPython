# list slicing means spliting the lists

list1 = ["apple","banana","mango","orange","kiwi","dates"]
print(list1[1:5])#prints only till index 4
print(list1[:5])#prints from 0 to 4
print(list1[:])#everything will be printed
print(list1[4:])#prints from index 4 to end

print(list1[:-1])# prints from the start to the element before the last one
print(list1[:-3])# prints form the start to the element before the third one from the last
print(list1[-3:])# prints from the third element from the last to the end


# Program to ask user to enter 10 numbers and save them to a list. find the max and min

i=1
listNumbers = []
for i in range(10):
    listNumbers.append(int(input("Please enter the number:- ")))

print("Max:- ",max(listNumbers))
print("Min:- ",min(listNumbers))

# program to print from the 2nd index of a list

listNew = [2,5,7,8,9]
print(listNew[2:])