# class A:
#     name='awal islam'

# a=A()
# # print(a.name)

# class B:
#     def __init__(self,name):
#         self.balance=100
#         self.name=name


# b=B('afdss')
# print(b.balance)
# print(b.name)


#nested class

class outer:
    def __init__(self,a):
        self.name='outer'

    class Inner:
        def __init__(self,b):
            self.name='inner'

        def show(self):
            print(self.name)

# Access nested class using outer object
# outer_object=outer()
# inner_object=outer_object.Inner()
# inner_object.show()
# access using outer class name

inner_object=outer.Inner(10)
inner_object.show()