'''
print pattern # # # #
              # # # #
              # # # #
              # # # # '''
# method 1
# print("# # # #")
# print("# # # #")
# print("# # # #")
# print("# # # #")

#method 2
'''for j in range(4):
    print("# ",end="")
print()
for j in range(4):
    print("# ",end="")
print()
for j in range(4):
    print("# ",end="")
print()
for j in range(4):
    print("# ",end="")'''

#method 3
'''
for i in range(4):
    for j in range(4):
        print("# ",end="")
    print()
'''
'''
print #
      # # 
      # # #
      # # # # 
'''
'''
for i in range(4):
    for j in range(i+1):
        print("# ",end="")
    print()
'''
'''
print # # # #
      # # #
      # #
      #  
'''
# for i in  range(4):
#     for j in range(4-i):
#         print("# ",end="")
#     print()

# Assignment Question
'''
1) print   1 2 3 4
           2 3 4
           3 4
           4
2) print   A P Q R
           A B P Q
           A B C R
           A B C D 
'''
# for i in range(4):
#     for j in range(i+1,5):
#         print(j,end="")
#     print()

for i in range(4):
    for j in range(4):
        if i<j:
            print(chr(65+14+j), end=" ")
        else :
            print(chr(65+j), end=" ")
    print()