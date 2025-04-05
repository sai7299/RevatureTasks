# class Account:
#     def __init__(self,acc_no,password):
#         self.acc_no=acc_no
#         self.__password=password
#     def reset_password(self):
#         print(self.__password)
# acc1=Account(12345,"sai")
# print(acc1.acc_no)
# print(acc1.reset_password())

class Person:
    __name="Sai"
    
    def __hello(self):
        print("hello person!")
        
    def welcome(self):
        self.__hello()

p1=Person()
print(p1.welcome())
        
        