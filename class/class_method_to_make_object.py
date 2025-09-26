class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, age, salary = data.split(",")
        return cls(name, int(age), float(salary))

emp = Employee.from_string("John,30,50000")
print(emp.name, emp.age, emp.salary)
