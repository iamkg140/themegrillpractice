# PUBLIC ACCESS MODIFIER - ASSESSED EVERYWHERE 
class A:
    def xyz(self):
        print("Hi")

class B:
    def abc(Self):
        print("Hello")
        # ob1 is object of class A
        ob1 = A()
        # calling A class ko xyz function 
        ob1.xyz()

ob = A()
ob.xyz()
# HERE HI WILL BE PRINTED 

ap = B()
ap.abc()
# HERE BOTH HELLO AND HI WILL BE PRINTED 

# PROTECTED ACCESS MODIFIER - underscore
# CANNOT BE CALLED ANYWHERE 
# IN INHERITED CLASS WE CAN ACCESS  
class A:
    def _xyz(self):
        print("Hi")

class B:
    def abc(Self):
        print("Hello")
        ob1 = A()
        ob1._xyz() #CAN BE CALLED ON INHERITED CLASS


# PRIVATE ACCESS MODIFIER - double underscore
# CAN BE ASSESSED ONLY IN SAME CLASS 
#  

        

