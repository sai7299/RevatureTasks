# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("Car Started..")

# car1=Car()
# car1.start()

class Car:
    brand="Mercedes"
    color="blue"
    def initial(self,acc,brake,clutch):
        self.acc=False
        self.brake=False
        self.clutch=False
    def start(self):
        self.acc=True
        self.clutch=True
        print("Car started")
c1=Car()
print(c1.start())
        