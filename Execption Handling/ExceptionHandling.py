#Handling exception and not stopping the flow

# try:
#     b = int(input("Enter a number:- "))
#     c = int(input("Enter a number:- "))
#     a = b/c
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#     print("Division is complete")



try:
    r = int(input("Enter a number:- "))
    if r<0:
        raise ValueError("Number cannot be negative")
except ValueError as v:
    print(v)

try:
    op = open("text.txt","r")
except IOError:
    print("File not present")
else:
    print("File not found")


#exception chaining