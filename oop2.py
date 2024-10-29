# create a class called person, that has three attributes, name, age, gender
# Then create a constructor method and method and object

class Person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(f"My name is {self.name} I am {self.age} and I am a {self.gender} ")

myobj =Person("Florence", 20, "Female")
myobj.display()

