x = int(input("Enter x value : "))
#r = x%2
if x%2:
    print("{} is Odd".format(x))
else:
    print("{} is even".format(x))
    if x>5:
        print("Great")
    else:
        print("Not Great")

y = int(input("Enter y value : "))
if y==1:
    print("One")
elif y==2:
    print("Two")
elif y == 3:
    print("Three")
elif y==4:
    print("Four")
else:
    print("Vlaue is Either 0 or Grater than 4")