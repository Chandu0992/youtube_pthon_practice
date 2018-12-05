a = 10 #global variable

'''
def myvar():
    #global a
    a = 15 #local variable
    print(a)
    print(id(a))


myvar()
print(a)
print(id(a))'''

def something():
    a = 9
    x = globals()['a']
    print("Inside of function : ",a)
    print(id(x))
    globals()['a'] = 20

something()
print(a)
print(id(a))