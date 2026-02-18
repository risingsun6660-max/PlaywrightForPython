# Iterative binary search

# def iterativeBinarySearch(list1,element):
#     low = 0
#     high = len(list1)
#     mid = 0
#     print(high)
#     while low<high:
#         mid = (high+low)//2
#         print(mid)

#         if list1[mid]<element:
#             low = mid+1
#         elif list1[mid]>element:
#             high = mid-1
#         else:
#             return mid
#     return -1

# list1 = [2,4,6,8,10,12,14]
# element = 12

# result = iterativeBinarySearch(list1,element)

# if result != -1:
#     print("element is present at index:- ",result)
# else:
#     print("element is not present")


#recursive binary search
#the function will call itself recursively until the element os found

def recursiveBinarySearch(low,high,element,list2):
    if low<=high:
        mid = (low+high)//2
        print(mid)
        if list2[mid] == element:
            return mid
        elif list2[mid]>element:
            return recursiveBinarySearch(low,mid-1,element,list2)
        else:
            return recursiveBinarySearch(mid+1,high,element,list2)
    return -1

list2 = [1,3,5,7,9,11,13,15,17]
element = 9

result1 = recursiveBinarySearch(0,len(list2),element,list2)
if result1 != -1:
    print("Element is present at index:- ",result1)
else:
    print("Element is not present")