#Video 38
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return even,odd


lst = [20,25,14,19,16,24,28,47,26]
even,odd = count(lst)
print("Even : {} and odd : {}".format(even,odd))

#Assignment
# Take 10 names from the user and then count and display The no of users
# who has more than 5 letters
n = int(input("Enter no of persons : "))
name_lst = []
for i in range(n):
    name_lst.append(input("Enter next name : "))

for i in name_lst:
    if len(i)>5:
        print(i)
#print(name_lst)