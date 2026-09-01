#Create a Student class.
class Student:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age

    def display(self):
        print(f"Student Name={self.name}")
        print(f"Student Age={self.age}")

S1=Student("Name",21)
S1.display()

#Create 3 objects of Student.
class Student:
    def __init__(self,name:str,age:int,gender:str):
         self.name=name
         self.age=age
         self.gender=gender

    def display(self):
         print(f"Student Name:{self.name}")
         print(f"Student Age:{self.age}")
         print(f"Student Gender:{self.gender}")
         print("-"*20)

S1=Student("Zahid",21,"Male")
S2=Student("Arosh",22,"Female")
S3=Student("Furkhan",12,"Male")
S1.display()
S2.display()
S3.display()


# Create a Car class with brand, model and price.
class Car:
    def __init__(self, brand: str, model: str, price: int)-> None:
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"Brand of a Car is:{self.brand}")
        print(f"Model of a Car is:{self.model}")
        print(f"Price of a Car is:{self.price}")


C = Car("Benz", "Mercides", "2000000")
C.display()

#Create a Person class and initialize name and age.
class Person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age

    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")

P1=Person("Zahid",21)
P1.display()

#Create a Book class with title and author.
class Book:
    def __init__(self,title:str,author:str)->None:
        self.title=title
        self.author=author

    def display(self):
        print(f"Title of a Book is:{self.title}")
        print(f"Author of the Book is:{self.author}")

B1=Book("Coding with Khan","Zahid Khan")
B1.display()

#Create a Rectangle class and calculate area.
class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def display(self):
        print(f"Area of a Rectangle is:{self.l*self.b}")

R1=Rectangle(10,20)
R1.display()

#Create a Circle class and calculate area.
class Circle:
    def __init__(self,r):
        self.r=r

    def display(self):
        print(f"Area of a Circle is:{3.14*self.r**2:.0f}")

C1=Circle(3)
C1.display()

#Create a BankAccount class with account number and balance.
class BankAccount:
    def __init__(self,acc_number:int,balance:int):
        self.acc_number=acc_number
        self.balance=balance

    def display(self):
        print(f"Account number:{self.acc_number}")
        print(f"Balance:{self.balance}")

B1=BankAccount(8147642073,50000)
B1.display()

#Create a Laptop class and display its details.
class Laptop:
    def __init__(self,RAM:int,SSD:str,Processor:str)->None:
        self.RAM=RAM
        self.SSD=SSD
        self.Processor=Processor

    def display(self):
        print(f"RAM of a Laptop is:{self.RAM}")
        print(f"SSD of a Laptop is:{self.SSD}")
        print(f"Processor of Laptop is:{self.Processor}")

L1=Laptop(12,"1TB","Intel")
L1.display()

#Create a Mobile class with brand, model and price.
class Mobile:
    def __init__(self,brand:str,model:str,price:int):
        self.brand=brand
        self.model=model
        self.price=price

    def display(self):
        print(f"Mobile brand is {self.brand}, Mobile model is {self.model} and the price of a mobile is {self.price}")

M1=Mobile("VIVO","Y28 5G",15000)
M1.display()

#Create a Student class with marks and calculate average.
class Student:
    def __init__(self,marks:list[int]):
        self.marks=marks

    def avg(self):
        total=sum(self.marks)
        avg=total/len(self.marks)
        print(f"Average:{avg:.0f}")

S1=Student([90,98,80,98,48])
S1.avg()

#Create an Employee class with name and salary.
class Employe:
    def __init__(self,name:str,salary:int):
        self.name=name
        self.salary=salary

    def display(self):
        print(f"Employee name is {self.name} and the salary of that employee is {self.salary}")

E1=Employe("Zahid","100000")
E1.display()

#Create a Product class with name, price and quantity.
class Product:
    def __init__(self,name:str,price:str,quantity:int):
        self.name=name
        self.price=price
        self.quantity=quantity

    def display(self):
        print(f"Product name is {self.name}, price of the prodect is {self.price} and the quantity of the prodect is {self.quantity}")

P1=Product("Mobile",20000,20)
P1.display()

#Create a Movie class with title, rating 
class Movie:
    def __init__(self,title:str,rating:int):
        self.title=title
        self.rating=rating

    def display(self):
        print(f"Title of the movie is {self.title} and the rating for that movie is {self.rating}")

M1=Movie("Pathan",4.5)
M1.display()