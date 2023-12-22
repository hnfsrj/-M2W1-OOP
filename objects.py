import unittest
from abc import ABC,abstractmethod


class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        return f"Make: {self.make} | Model: {self.model} | Year: {self.year}"

    
class ElectricCar(Car):
    def __init__(self,make,model,year,battery_capacity):
        Car.__init__(self,make,model,year)

        self.battery_capacity = battery_capacity

    def charging_time(self):
        return f"{self.battery_capacity/2000} hrs"

    












class BankAccount:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.__balance = 0

    def deposit(self,amount):
        if amount >= 0:
            self.__balance += amount
            return self.__balance
        else:
            return "invalid"

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            return "invalid"

    def balance(self):
        return f"Your balance is : {self.__balance}"









class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return (2*3.14*(self.radius**2))
    

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height =height

    def calculate_area(self):
        return (self.width*self.height)



class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return (0.5*self.base*self.height)



shape1 = Circle(2)
shape2 = Rectangle(2,4)
shape3 = Triangle(4,8)


print(shape1.calculate_area())
print(shape2.calculate_area())
print(shape3.calculate_area())










class Testing_BankAccount(unittest.TestCase):
    def setUp(self):
        self.customer = BankAccount("Hanif","Siraj")

    def test_deposit(self):
        self.assertEqual(self.customer.deposit(100),100)

    def test_invalid_deposit(self):
        self.assertEqual(self.customer.deposit(-200),"invalid")

    def test_withdraw(self):
        self.customer.deposit(100)

        self.assertEqual(self.customer.withdraw(50),50)

    def test_invalid_withdraw(self):
        self.customer.deposit(100)

        self.assertEqual(self.customer.withdraw(200),"invalid")

    def test_balance(self):
        self.customer.deposit(100)
        self.customer.withdraw(50)

        self.assertEqual(self.customer.balance(),"Your balance is : 50")


if __name__ == "__main__":
    unittest.main()