#import array as arr
from array import *

vals = array('i',[5,9,-8,4,2]) #'i' will take -ve and +ve values
'''#vals = array('I',[5,9,-8,4,2]) #'I' will give an error OverflowError: can't convert negative value to unsigned int
# 'I' will consider from 0 t0 +ve number's if remove -ve sign in the above arrary code will execute
print(vals.buffer_info()) # gives address and size of the array
print(vals.typecode)
vals.append(20)
print(vals)
vals.reverse()
print("Checking")
print(vals[0])

for i in range(len(vals)):
    print(vals[i])

print("Another Method : ")
for x in vals:
    print(x)'''

newArr = array(vals.typecode,(a*a for a in vals))
for e in newArr:
    print(e)

# while loop also work but take extra lines of work to make it sense
# i = 0
# while i<len(newArr):
#     print(newArr[i])
#     i += 1
