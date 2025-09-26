class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Shop:
    product=[]

    def add_product(self,product):
        if isinstance(product,(dict,str)):
            print('please using list tuple and set to add multiple  product')
            return
        # if type(product)==list or  type(product)==tuple:
        if isinstance(product,(list,tuple,set)):
            self.product.extend(product)
        else:
         self.product.append(product)

    def show_product(self):
        for p in self.product:
            print(f'{p.name}-----{p.price}')
S=Shop()

p1=Product('alu',20)
p2=Product('potl',30)
p3=Product('trkari',40)

S.add_product(p1)
S.add_product([p2,p3])
S.add_product({p1,p2,p3})
S.show_product()
