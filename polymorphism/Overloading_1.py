class Math:
    def add(self, *args):
        return sum(args)

m = Math()
print(m.add(10))          
print(m.add(10, 20))      
print(m.add(10, 20, 30))  
