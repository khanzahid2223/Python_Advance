#Create different classes with the same method name sound().
class A:
    def sound(self):
        print("Sound of A")

class B:
    def sound(self):
        print("Sound of B")

class C:
    def sound(self):
        print("Sound of C")

class D:
    def sound(self):
        print("Sound of D")

lst=[A(),B(),C(),D()]
for i in lst:
    i.sound()

#Create Dog, Cat and Cow with different sound() implementations.
class Dog:
    def sound(self):
        print("Woof!")

class Cat:
    def sound(self):
        print("Meow!")

class Cow:
    def sound(self):
        print("Ambaa!")

Animal=[Dog(),Cat(),Cow()]
for a in Animal:
    a.sound()

#Create Car and Bike with the same move() method.
class Car:
    def move(self):
        print("Car moves faster then Bike")

class Bike:
    def move(self):
        print("Bike move slower than Car")

Vehical=[Car(),Bike()]
for v in Vehical:
    v.move()

#Create Developer and Designer with the same work() method.
class Developer:
    def work(self):
        print("Developer will develope websites")

class Designer:
    def work(self):
        print("Designer will desing the structure of the website")

Engineer=[Developer(),Designer()]
for e in Engineer:
    e.work()

#Create different payment classes with pay() method.
class Paytm:
    def pay(self):
        print("Pay through Paytm")

class PhonePay:
    def pay(self):
        print("Pay through PhonePay")

class GooglePay:
    def pay(self):
        print("Pay through GooglePay")

Amount=[Paytm(),PhonePay(),GooglePay()]
for a in Amount:
    a.pay()

#Create different shapes with the same area() method.
class Shapes:
    def area(self):
        return 0

class Rectangle(Shapes):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(f"Area of Rectangle is:{self.l*self.b}")

class Circle:
    def __init__(self,r):
        self.r=r

    def area(self):
        print(f"Area of a Cricle is:{3.14*self.r**2}")

Shape=[Rectangle(2,5),Circle(5),Rectangle(10,5),Circle(2)]
for s in Shape:
    s.area()

#Create a notification system where Email, SMS and WhatsApp have send().
class Email:
    def send(self):
        print("Your notification has been sent successfully.")

class SMS:
    def send(self):
        print("Your SMS has been sent successfully.")

class WhatsApp:
    def send(self):
        print("Your WhatsApp message has been sent successfully.")

App=[Email(),SMS(),WhatsApp()]
for a in App:
    a.send()