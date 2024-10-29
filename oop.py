class Fruits:
    # constructor
    def __init__(self, price, shape, name):
        self.price = price
        self.shape = shape
        self.name = name
    def display(self):
        print(f"My favorite fruit is {self.name} and its {self.shape} in shape and costs {self.price}")

# create instance of a class

myobj =Fruits(20, "oval", "Banana")
myobj.display()



