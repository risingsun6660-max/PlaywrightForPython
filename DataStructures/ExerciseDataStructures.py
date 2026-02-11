#Ask the user the name, parents name, grade and address and store them to a dictionary
#access and print the name
#change the address to a different one
#add a contact key
#print all the values in the dictionary using for loop


my_dict ={}
my_dict["Name"] = input("Enter the name:- ")
my_dict["Parents Name"] = input("Enter the parents name:- ")
my_dict["Grade"] = input("Enter the grade:- ")
my_dict["Address"] = input("Enter the address:- ")

print(my_dict)
print("The name is :- ",my_dict["Name"])
print("The parents name is :- ",my_dict["Parents Name"])
print("The grade is :- ",my_dict["Grade"])
print("The address is :- ",my_dict["Address"])


my_dict["Address"] = "Nottingham lane"
print("The new address is :- ",my_dict["Address"])


my_dict["Contact"] = "1234567"

for i in my_dict:
    print(i,":-",my_dict[i])


#create a set using the list [1,2,3,4,5,4,3,2,1]
#remove 5 from the list
#extend the set with {9,10,11,12}

list1 = [1,2,3,4,5,4,3,2,1]
my_set = set(list1)
print(my_set)

list1.pop(4)

my_set.update([9,10,11,12])
print(list1)
print(my_set)