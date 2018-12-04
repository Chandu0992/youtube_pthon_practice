from numpy import *
print("Enter Matrix A")
m = int(input("Enter no of rows : "))
n = int(input("Enter no of cols : "))
print("Enter Matrix B")
p = int(input("Enter no of rows : "))
q = int(input("Enter no of cols : "))
sum = 0
mat_A =[]
mat_B =[]
mat_C =[]

if n!=p:
    print("Matrix Multiplication is not Possible !")
else:
    for i in range(m):
        for j in range(n):
            mat_A.append(int(input("Enter element : ")))
    mat_A = array(mat_A).reshape(m,n)

    for i in range(p):
        for j in range(q):
            mat_B.append(int(input("Enter element : ")))
    mat_B = array(mat_B).reshape(p,q)

    mat_C = mat_A * mat_B
    # for i in range(m):
    #     for j in range(q):
    #         for k in range(p):
    #             sum = sum + mat_A[i][k] * mat_B[k][j]
    #         mat_C[i][j] = sum
    #         #mat_C[i][j].append(sum)
    #     sum = 0 #index out of range error is comming

print(mat_A)
print(mat_B)
print(mat_C)