
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("inhale, exhale")


class Fish(Animal):     #Fish class inherite from another class Animal
    def __init__(self):
        super().__init__()  #inheritance attributes and methods
        #super() refers to the super-class (Animal)
    def breath(self):
        super().breath()
        print("doing underwater")
    def swin(self):
        print("movig in water")

nemo = Fish()
nemo.swin()
nemo.breath()
print(nemo.num_eyes)
