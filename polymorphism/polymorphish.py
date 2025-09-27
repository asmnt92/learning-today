class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print('Animal sound')

class dog(Animal):

    def sound(self):
        print('buk buk buk')

class cat(Animal):
    def sound(self):
        print('meow meow meow')


