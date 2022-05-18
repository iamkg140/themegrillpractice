# INHERITANCE 
class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak() 

# CONSTRUCTOR 
class myClass:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname #varaiabel declare
        self.fullname = self.fname + ' ' +self.lname
        print('Constructor is called')
# CREATING ITS OBJECT 
obj1 = myClass('kanchan', 'gautam')
obj2 = myClass('ram', 'sharma')
print(obj1.fname)
print(obj2.fullname)

# DESTRUCTOR 
class myClass:
    def __init__(self):
        self.name = "Python"

    


