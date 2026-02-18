#normal way to double a list

num = [2,3,4,5,6,7,8]

double =[]

for i in num:
    double.append(i*2)

print(double)

#using list comprehence we double a list as below

newList = [x*2 for x in num]
print(newList)

#filtering odd numbers using list comprehension

oddNo = [x for x in range(30) if x%2 !=0]
print(oddNo)

#odd or even
oddOrEven = ["even" if x%2 == 0 else "odd" for x in range(21,30)]
print(oddOrEven)