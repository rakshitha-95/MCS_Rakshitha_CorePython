'''
class Myclass:
    x=3

p1=Myclass()
print(p1.x)


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("hello my name is "+self.name)


p=Person("Rakshitha",27)
print(p.name)
print(p.age)
p.myfunc()
'''

class Person:
    def __init__(myobject,name,age):
        myobject.name=name
        myobject.age=age

    def myfunc(self):
        print("tha name of the Person is "+self.name)
        print("the age of yhe person is "+self.age)

p1=Person("rakshiths", 26)
print(p1.name)
print(p1.age)
p1.myfunc()
p1.age=29
p1.name="varun"
print(p1.name)
print(p1.age)

class Student(Person):
    def __init__(self,name,age):
        Person .__init(self,name,age)

x=Student("Rakshitha",27)
print(p1.age)
print(p1.name)






