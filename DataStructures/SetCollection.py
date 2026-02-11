# a set is a unique collection of unordered elements
set1 = {1,2,3,2}# duplicate elements will be skipped
print(set1)

set2 = {1,10.0,"hello",(1,2,3)}
print(set2)

s = set()
print(s)
print(type(s))

#indexing is not allowed in set, that is you cannot retrieve data via index
#adding to set
my_set = {1,2,3}
my_set.add(4)
print(my_set)
my_set.update([5,6,7,8])
print(my_set)

#deleting from a set
#difference between discard and remove is that remove throws an error if element not present
my_set.discard(8)
print(my_set)
my_set.discard(10) # doesnt throw an error if the element is not present just ignores
print(my_set)
my_set.remove(7)
print(my_set)
my_set.remove(10) # throws key error if not present




