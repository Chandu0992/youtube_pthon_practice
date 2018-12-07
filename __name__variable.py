#import Calc
#print("Demo Says : ",__name__) #prints __main__

#video 46
from Calc import sum

def funOne():
    sum()
    print("From FunOne")

def funTwo():
    print("From FunTwo")

def main():
    funOne()
    funTwo()
main()