class GrandParent:
    def G_pshow(self):
        print('Grand Parent Class')

class Parent(GrandParent):
    def Pshow(self):
        print('Parent class')

class Child(Parent):
    def show(self):
        print('Child class')


child=Child()
child.show()
child.Pshow()
child.G_pshow()
