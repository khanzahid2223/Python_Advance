#Create a Vehicle parent class and Car child class.
class Vehicle:
    def __init__(self,brand):
        self.brand=brand

    def model(self):
        print(f"{self.brand} is a Vehicle")

class Car(Vehicle):
    def petrol(self):
        print(f"{self.brand} is Petrol type")

V1=Car("Benz")
V1.model()
V1.petrol()

#Create Animal → Dog.
class Animal:
    def eat(self):
        print("Animal will eat")

    def sleep(self):
        print("Amimal will sleep")

class Dog(Animal):
    def bark(self):
        print("Dog will bark")

D1=Dog()
D1.eat()
D1.sleep()
D1.bark()


#Create Person → Student.
class Person:
    def __init__(self,n,a):
        self.n=n
        self.a=a
        
    def name(self):
        print(f"Person's name is {self.n}")

    def age(self):
        print(f"Person's age is {self.a}")

class Student(Person):
    def __init__(self, n, a,ID):
        super().__init__(n, a)
        self.ID=ID
    def id(self):
        print(f"Student ID is {self.ID}")

S1=Student("Zahid",21,205)
S1.name()
S1.age()
S1.id()

#Create Employee → Manager.
class Employee:
    def name(self):
        print("Employee has a name")


    def id(self):
        print("Employee has ID")

class Manager(Employee):
    def team(self):
        print("Manager will handle a team")

M=Manager()
M.name()
M.id()
M.team()

#Create Shape → Rectangle.
class Shape:
    def shape(self):
        print("There are multiple shapes")

class Rectangle(Shape):
    def rect(self):
        print("This is one type of a shape")

R=Rectangle()
R.shape()
R.rect()

#Create Vehicle → Bike and Vehicle → Car.
class Vehicle:
    def __init__(self,brand):
        self.brand=brand

    def model(self):
        print(f"Vehicle's brand  is {self.brand}")

class Bike(Vehicle):
    def milage(self):
        print(f"{self.brand} will gives 70Km milage")

class Car(Vehicle):
    def fuel(self):
        print(f"{self.brand} is of Petrol")

B=Bike("Pulsar")
B.model()
B.milage()
print("***********************")
C=Car("Benz")
C.model()
C.fuel()

#Create Animal → Dog and Animal → Cat.
class Animal:
    def eat(self):
        print("Animal will eat")

    def sleep(self):
        print("Animal will sleep")

class Dog(Animal):
    def bark(self):
        print("Dog will bark")

class Cat(Animal):
    def meow(self):
        print("Cat will do meow sound")

D=Dog()
D.eat()
D.sleep()
D.bark()
print("*********************************")
C=Cat()
C.eat()
C.sleep()
C.meow()

#Create BankAccount → SavingsAccount.
class BankAccount:
    def name(self):
        print("BankAccount inclued name of the customer")

class SavingsAccount(BankAccount):
    def amount(self):
        print("SavingsAccount includes amount")

S=SavingsAccount()
S.name()
S.amount()

#Create BankAccount → CurrentAccount.
class BankAccount:
    def name(self):
        print("Customer name")

class CurrentAccount(BankAccount):
    def amount(self):
        print("This includes the amount")

C=CurrentAccount()
C.name()
C.amount()

#Create User → Admin.
class User:
    def name(self):
        print("Name of the user")

class Admin(User):
    def email(self):
        print("Email of the user")

    def password(self):
        print("Password to login")

A=Admin()
A.name()
A.email()
A.password()

#Create User → Customer.
class User:
    def name(self):
        print("Name of the user")

class Customer(User):
    def details(self):
        print("Details of the customer")

    def products(self):
        print("List of the prodects purchased by the customer")

    def bill(self):
        print("Final total bill of the products purchased by the customer")

C=Customer()
C.name()
C.details()
C.products()
C.bill()

#Create Employee → Developer.
class Employee:
    def name(self):
        print("Name of the employee")

    def ID(self):
        print("ID of the employee")

class Developer(Employee):
    def knowledge(self):
        print("The developer has the good knowledge of coding")

D=Developer()
D.name()
D.ID()
D.knowledge()

#Create Employee → Designer.
class Employee:
    def ID(self):
        print("Emolpyee has a unique ID")

    def name(self):
        print("Employee has a name")

class Designer(Employee):
    def plan(self):
        print("Employee has a designer plan")

D=Designer()
D.ID()
D.name()
D.plan()

#Create a multilevel hierarchy: Animal → Mammal → Dog.
class Animal:
    def eat(self):
        print("Animal can eat")

    def sleep(self):
        print("Animal can sleep")

class Mammal(Animal):
    def walk(self):
        print("Mammal can walk")

class Dog(Animal):
    def bark(self):
        print("Dog will bark")

M=Mammal()
M.eat()
M.sleep()
M.walk()
print("---------------------------")
D=Dog()
D.eat()
D.sleep()
D.bark()

#Create a hierarchical inheritance system for different types of employees.
class Emoloyee:
    def __init__(self,role):
        self.role=role
        
    def name(self):
        print(f"{self.role} has a name")

    def Id(self):
        print(f"{self.role} has a ID")

class Developer(Emoloyee):
    def skills(self):
        print(f"Developer has a good Programming skill")

    def project(self):
        print("Developer will work on real world projects")

class Manager(Emoloyee):
    def team(self):
        print("Manager will manage a team ")

    def lead(self):
        print("Manager act as a leader to manager their team")

class Tester(Emoloyee):
    def test(self):
        print("The Test Engineer will test there are any errors in a program")

    def bug(self):
        print("Test Engineer will recorrect the bugs in a program")

D=Developer("Developer")
D.name()
D.Id()
D.skills()
D.project()
print("-------------------------------------------------")
M=Manager("Manager")
M.name()
M.Id()
M.team()
M.lead()
print("-------------------------------------------------")
T=Tester("Tester")
T.name()
T.Id()
T.test()
T.bug()