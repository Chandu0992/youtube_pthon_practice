class A:
    def show(self):
        print("From  Class A !")
class B:
    def show(self):
        print("From  Class B !")

class C(A,B):
    def view(self):
        print("From Class C")

d = C()
d.show()
    
