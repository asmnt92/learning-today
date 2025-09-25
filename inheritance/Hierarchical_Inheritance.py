class Parent:
    blood='*&%$#@'


class Child1(Parent):
    
    def show(self):
        print(f'child1 carry father blood {self.blood}')

class Child2(Parent):
    
    def show(self):
        print(f'child2 also carry father blood {self.blood}')



Child1().show()
Child2().show()