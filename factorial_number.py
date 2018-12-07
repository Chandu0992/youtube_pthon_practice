#video 39
'''
def fact(p):
    f = 1
    for i in range(1,p+1):
        f = f*i
    return f



x = int(input("Enter a value to get factorial : "))

res = fact(x)
print("factorial of {} is {}".format(x,res))

#Video 40
#Recursion
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i = 0
def greet():
    global i
    i += 1
    print("Hello", i)
    greet()
'''
#near by 2000 it will give the error of
#RecursionError: maximum recursion depth exceeded while calling a Python object

#Video 41

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

x = int(input("Enter a value : "))
res = fact(x)
print("Factorial of {} is {}".format(x,res))