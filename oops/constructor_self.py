#Video 49(local)/50(youtube)
'''
class Computer:
    def __init__(self):
        self.name = 'Chandu'
        self.age = 25

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False



c1 = Computer() #Constructor init method calls internally not explicitly
print(id(c1))
#c1.age=30
c2 = Computer() #Constructor init method calls internally not explicitly
print(id(c2))


if c1.age == c2.age:
    print("Same !")
else:
    print("Different")
if c1.compare(c2):
    print("They are same !")'''

#Video 51(local)/52(Youtube)
'''
class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.company = 'BMW'

c1 = Car()
c2 = Car()
c2.mil = 15
c2.company='Jagur'
#Car.wheels = 5
print(c1.company,c1.mil,Car.wheels)
print(c2.company,c2.mil,Car.wheels)'''

class Student:

    school = 'Little JK Public School'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def school_name(self):
        return self.school

    @staticmethod
    def info():
        print("This is Static Method !")

s1 = Student(35,45,55)
s2 = Student(45,40,60)

print(s1.avg())
print(s2.avg())

print(s1.m1)
s1.m1 = 20
print (s1.m1)
print(Student.school_name())
Student.info()














