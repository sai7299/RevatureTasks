#multilevel -->base-child-child
class Car:
    def __init(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class Toyotacar(Car):
    def __init__(self,name):
        self.name=name
        
car1=Toyotacar("fortuner")
car2=Toyotacar("virtus")
print(car1.name)
print(car1.start())

class Fortuner(Toyotacar):
    
    def __init__(self,type):
        self.type=type
        
car3=Fortuner("diesel")
print(car3.type)
car3.start()

#multiple-->two base and one child
class A:
    varA="Welcome to class A"
class B:
    varB="Welcome to class B"
class C(A,B):
    varC="welcome to class C"
c=C()
print(c.varC) 

#super

class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")

class Toyotacar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)  # Corrected to call super().__init__(type)

# Creating an instance of Toyotacar
car1 = Toyotacar("prius", "electric")
print(car1.type)  # Output: electric
