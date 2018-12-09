from functools import reduce
#Video 42
f = lambda a : a*a
print("Square of 5 is {}".format(f(5)))

#Video 43
def is_even(i):
    return i%2==0

def is_odd(i):
    return i%2!=0

nums = [3,2,6,8,4,6,2,9]
evens = list(filter(is_even,nums))
odd = list(filter(is_odd,nums))

print(evens)
print(odd)

l_even = list(filter(lambda n : n%2==0,nums))
print(l_even)

doubles = list(map(lambda n : n*2,l_even))
print(doubles)

sum = reduce(lambda a,b : a+b,doubles)
print(sum)
