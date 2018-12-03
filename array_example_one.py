'''from array import *

arr = array('i',[])
n = int(input("Please Enter size of the array : "))
for i in range(n):
    x = int(input("Enter next  Value : "))
    arr.append(x)

#manual method
print(arr)
s = int(input("Enter a Value to search : "))
k = 0
for i in arr:
    if i == s:
        print(k)
        break
    k += 1
if s not in arr:
    print("Element not Found !")

#Inbulit Method
print(arr.index(s))
'''
#Assignment Questions
#1) Create an array with 5 values and delete the value at index number 2 without using in-built function
#2) write a code to reverse an array without using in-built function

from array import *

arr = array('i',[])
n = int(input("Enter size of an array : "))
for i in range(n):
    x = int(input("Please Enter a value : "))
    arr.append(x)
print(arr)
s = int(input("Enter value to delete : "))
for i in arr:
    if i == s:
        #arr.remove(s) #delete the particular element
        #del arr[i] #delete the element at ith iendex
        arr.remove(s)
        break
print("After deletion array : ",arr)