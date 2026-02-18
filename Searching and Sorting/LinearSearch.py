# Linear search or sequential search
# compares the element one by one with all the lements in the list

def linearSearch(listToBeSearched,n,element):
    for i in range(0,n):
        if listToBeSearched[i] == element:
            return i
        
    return -1


listToBeSearched = [2,13,24,35,46,57,68,79,88,99]

n = len(listToBeSearched)
element = 57
result = linearSearch(listToBeSearched,n,66)

if result == -1:
    print("element not found")
else:
    print("elemet present")