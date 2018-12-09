from numpy import *

#Three Dimensional Array
arr = array(
    [
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
         ],
        [
            [9,8,7],
            [6,5,4],
            [3,2,1]
        ],
        [
            [1,5,9],
            [7,5,3],
            [5,4,6]
        ]
    ]
)

'''print(arr)  #prints array
print(arr.dtype) #prints data type
print(arr.ndim) #prints how many dimensions
print(arr.shape) #gives a tuple that contains no.of rows and no.of cols
arr1 = arr.flatten()
print(arr.flatten()) # creates one dim array
#print(id(arr))
#print(id(arr1))
print(arr1.reshape(3,9)) #prints 2d of 3X9 matrix'''

#arr1 = (arr.copy()).reshape(3,9)
'''m = matrix(arr1)
print(arr)
print(arr1)
print(id(arr))
print(id(arr1))
print(m)
print(id(m))'''

m = matrix('1 2 3 ; 4  5 6')
m1 = matrix('9 8 ; 7 6 ; 5 4')
print(m)
print(diagonal(m))
print(m.min())
print(m.max())
m3 = m * m1
print(m3)
print(type(arr))


















