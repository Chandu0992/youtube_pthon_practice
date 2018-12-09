#av = 10
x = int(input("Check Given number is prime or not : "))
#i = 1
'''if x>av:
    print("Bye")
    pass
else:
    while i<=x:
        print("Candy")
        i += 1'''
'''while i<=x:
    if i>av:
        print("bye,Out of Stock!")
        break
    print("Candy")
    i += 1'''
# pass
'''for i in range(1,101):
    if i%2 != 0:
        pass
    else:
        print(i)'''

#print first 50 fibonacci numbers
#Check a given number is prime or not
a,b,c = 0,1,0
#while b<51:
print(a)
for i in range(51):
    print(b)
    a,b = b,a+b
    c += 1
print("No of Fibonacci numbers : ",c)
if x>1:
    for i in range(2,x):
        if x%i == 0:
            print("{} is not prime number !".format(x))
            break
    else:
        print("{} is prime number !".format(x))
else:
    print("{} is not prime!".format(x))