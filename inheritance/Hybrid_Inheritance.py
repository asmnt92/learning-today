class A:
    a=10


class B(A):
    b=A.a+10

class C:
    c=30

class D(B,C):
    D=B.b+C.c
    
    def __init__(self):
        super().__init__()
        print(self.D)


D()

