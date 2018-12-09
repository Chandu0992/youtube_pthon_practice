#Functions
#What is function
#Why Function
#Creating and Calling Function

#Video 33
'''
def greet(): #Function Definition
    print("Hello")
    print("Good Morning!")

greet() #Function calling
#greet()


def add(a,b):
    greet()
    return a+b

print(add(4,5))

#Video 34
#Function Arguments
#Types of Arguments
'''
'''
def update(x): #Function with arguments #Formal arguments
    print(x)
    print(id(x))
    #x = 8
    x[1] = 25
    print(id(x))
    print(x)
'''
'''a = 10
print(id(a))
update(a) #Actual Arguments
print("a : ",a) #Pass by Value'''
'''
lst = [10,20,30]
print(id(lst))
update(lst) #Actual Arguments
print("list : ",lst) #Pass by Value
print(id(lst))
'''
#video 35

'''def add(a,b): #Formal Arguments
    c = a+b
    print(c)

add(5,4) #Actual Arguments
'''
'''def Person(name,age):
    print("Name : ",name)
    print("Age : ",age-5)

#Person('Chandu',25)
#Person(25,'Chandu') #error unsupported operand type str and int
Person(age=25,name='Chandu') #Named Arguments
'''
'''
def sum(*b): #Formal Arguments
    c = 0
    for e in b:
        c += e
    print(c)

#sum(5,4,36,89) #Actual Arguments #variable length arguments no of variable are not fixed
#sum() takes 2 positional arguments but 4 were given
#sum(5,4,36,89)
#TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
sum(5,4,36,89)
sum(5)
sum(4,6)
'''
#Video 36

def person(**data):
    #print(name)
    #print(data)
    for i,j in data.items():
        print(i,j)

person(name='Chandu',age=25,city='Srikakulam',mob=8008922974)