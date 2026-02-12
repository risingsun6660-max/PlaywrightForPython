my_String = '''John is
a python expert'''#multi line string

print(my_String)

print(my_String[0])
print(my_String[4:-1])


#string concatenation
str1 = "hello"
str2 = "world"

print(str1+" "+str2)
print(str2*6)

str3 = 404

#cannot concatenate string with an integer directly
#workaround is type casting

print(str1+str2+str(str3))


#string membership test
print("o" in "john")
print("oh" in "john")
print("oh"  not in "john")

print("a" in "john")
print("on" in "john")

#iteration in string
count =0
for letter in "simran kumari is showing python":
    if letter=="i":
        count = count + 1
print(count)

noOfLetters =0
for letter in "simran kumari is showing python":
    noOfLetters = noOfLetters+1
print(noOfLetters)


#other functions with string

str5 =  "simran kumari is showing python"
print(list(enumerate(str5)))
print(len(str5))



