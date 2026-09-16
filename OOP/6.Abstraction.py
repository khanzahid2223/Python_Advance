#Create an abstract Vehicle class.
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def fuel(self):
        pass

class Car(Vehicle):
    def __init__(self,n,f):
        self.n=n
        self.f=f

    def name(self):
        print(f"The Car name is {self.n}")

    def fuel(self):
        print(f"{self.n} uses {self.f}")

C=Car("Benz","Petrol")
C.name()
C.fuel()

#Create abstract Shape with an area() method.
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return self.l*self.b

R=Rectangle(10,5)
print(R.area())

#Implement Circle and Rectangle from Shape.
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.r=r

    def area(self):
        print(f"Area of a Circle is:{3.14*self.r**2}")

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        print(f"Area of Rectangle is:{self.l*self.b}")

C=Circle(2)
C.area()
R=Rectangle(10,8)
R.area()

#Create an abstract Payment class.
from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class PhonePay(Payment):
    def __init__(self,amount):
        self.amount=amount

    def pay(self):
        print(f"Payment recived on PhonePay ₹{self.amount}")

class Paytm(Payment):
    def __init__(self,amount):
        self.amount=amount

    def pay(self):
        print(f"Payment recives on Paytm ₹{self.amount}")

P=PhonePay(20000)
P.pay()
P1=Paytm(30000)
P1.pay()