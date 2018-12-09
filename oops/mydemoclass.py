#video 47(local)/48(youtube)

class Computer():
    #Attributes #Variables
    #Behavior #Methods(Functions)
    def config(self):
        print("i5, 8gb, 1TB")

comp1 = Computer()
comp1.config()
print(type(Computer.config(comp1))) #None Type
# conf2 = Computer
# conf2.config() #TypeError: config() missing 1 required positional argument: 'self'

#video 48(local)/49(youtube)

class myComputer:

    def __init__(self,cpu,ram): #Constructor
        self.cpu = cpu
        self.ram = ram
        #print("In init !")

    def config(self):
        print("Cpu : {} and Ram : {}".format(self.cpu, self.ram))

conf = myComputer('i5',8)
confOne = myComputer('i7',16)

conf.config()
confOne.config()