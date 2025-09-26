class Student:
    school_name = "ABC School"  

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name


s1=Student('Awal')
print(f'name : {s1.name}\nSchool name : {s1.school_name}')

# change school name using class method 
s1.change_school('Khaya Pori Suti')
print(f'name : {s1.name}\nSchool name : {s1.school_name}')