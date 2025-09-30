class Shopping:
    card=[] #class attribute | static attribute
    brand='KA KA Tu Ya'

    def __init__(self,name,location):
        self.name=name
        self.location=location

    def purchase(self,item,price):   #instance method
        print(f'buying {item} price {price}')

    @classmethod
    def hudai(cls,am):  #class method
        print(f"hudai am jnota . com {am}")

    @staticmethod
    def dekhi(deo): #static method
        print(f'Dilam Dekhiye {deo}')

# Shopping.purchase('a',30)
# s=Shopping('Baksi','cadni,tari ')
# s.purchase('abc',20)
# Shopping.hudai('hudai')
Shopping.dekhi('Pakhi')

