from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print('Car start')



c=Car()
print(issubclass(Car,Vehicle))
print(isinstance(c,Car))