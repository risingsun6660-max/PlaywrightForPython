#for <loop variable> in <iterable>
    #body of loop

#in is also called inclusion operator
#range(<start>,<stop>,<step>)

# for i in range(1,10,1): #prints only till 9 and not 10
#     print(i)

# for j in range(1,11,1): #prints till 10
#     print(j)

#start and step in range function can be skipped

for k in range(1,11):#step is skipped so by default its taken as 1
    print(k)

for l in range(11,2):#doesnt print as this is taken as start and stop, as start is greater than stop
    print(l)


for m in range(11):# start is by default from 0 and step by default as 1
    print(m)

# if we skip the start then step value should also be skipped otherwise it will take the step value as stop value

for n in range(10,1,-1): # to print in the reverse form 10 to 1
    print(n)