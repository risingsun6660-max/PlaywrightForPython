#escape sequences

print('''She said,"I saw a ghost'? Did you even"''')

print('She said,"I saw a ghost\'? Did you even"')

print("She said,\"I saw a ghost'? Did you even\'")

print("simran kumari \nis showing python")
print("simran kumari \tis showing python")
print("simran kumari \vis showing python")


#format function

sent = "{},{},{}".format("simran","mizhi","dolly")
print(sent)

sent = "{s},{m},{d}".format(s="simran",m="mizhilly",d="dolly")
print(sent)

sent = "{0},{1},{2}".format("simran","mizhi","dollilly")
print(sent)

print(1/3)
print("{0:.2f}".format(1/3))


#string methods
print("johnWALTER".lower())
print("johnWALTER".upper())


str2=  "simran kumari is showing python"
a = (str2.split())
print(a)

print(" ".join(a))