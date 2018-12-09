#28th video
from numpy import *

#arr = array('i',[1,2,3],[2,5,4])
#arr = array([1,2,3,4,5])
#print(arr)

#29th video

#No.of ways to create an array
#array()
#linspace()
#logspace()
#arange()
#zeros()
#ones()
'''arr = array([1,2,3,4,5.0]) #folat64
arr = array([1,2,3,4,5])
print(arr.dtype) #int32
arr = array([1,2,3,4,5],float)
print(arr.dtype) #float64

#linspace

arr = linspace(0,15,16) #(start,end,no.of parts)
arr = linspace(0,15)
print(arr)
'''

#arange
#arr = arange(1,15,2) #(start,end,step)
arr = logspace(1,40,5)
#arr = logspace('%.2f' %arr[4])
'''print(arr)

arr = zeros(5,int)

print(arr.dtype) #int32

arr = zeros(5)

print(arr)#float64

#video 30

arr = array([1,2,3,4,5])
arr += 5
print(arr)

arr1 = array([6,7,8,9,10])

sum = arr+arr1

arr= array([1,2,3,4,5])
print(cos(arr[0]))

arr2 = arr1.view()  #shallow copy
arr2 = arr1.copy()  #deep copy
arr1[1] = 5
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))'''

#Assignment
# 1)Write a code to add 2 arrays using for loop
# 2) write a code to find the maximum value from an array without using bulit-in function

#1) Solution

arr = array([1,2,3,4,5])
arr1 = array([1,2,3,7,5])
arr2 = []
for i in range(len(arr)):
    arr2.append(arr[i]+arr1[i])
print(arr2)

#2) Solution
ele = 0
for i in arr2:
    if i>ele:
        ele = i
print("max element : ",ele)
