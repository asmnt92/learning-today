class Person:
    def show_info(self, **kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

p = Person()
p.show_info(name="Alice")  
p.show_info(name="Bob", age=25)  
p.show_info(name="Charlie", age=30, city="New York")
