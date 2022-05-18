# CREATING CLASS 
class myClass:
    number = 20

# CREATING OBJECT 
obj = myClass()
print(obj.number)


# EXAMPLE 2 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Taylor", 32)

print(p1.name)
print(p1.age)