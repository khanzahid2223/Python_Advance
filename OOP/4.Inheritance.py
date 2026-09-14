"""
Create Shape → Rectangle.
Create Vehicle → Bike and Vehicle → Car.
Create Animal → Dog and Animal → Cat.
Create BankAccount → SavingsAccount.
Create BankAccount → CurrentAccount.
Create User → Admin.
Create User → Customer.
Create Employee → Developer.
Create Employee → Designer.
Create a multilevel hierarchy: Animal → Mammal → Dog.
Create a hierarchical inheritance system for different types of employees.
"""
# #Create a Vehicle parent class and Car child class.
# class Vehicle:
#     def __init__(self,brand):
#         self.brand=brand

#     def model(self):
#         print(f"{self.brand} is a Vehicle")

# class Car(Vehicle):
#     def petrol(self):
#         print(f"{self.brand} is Petrol type")

# V1=Car("Benz")
# V1.model()
# V1.petrol()

# #Create Animal → Dog.
# class Animal:
#     def eat(self):
#         print("Animal will eat")

#     def sleep(self):
#         print("Amimal will sleep")

# class Dog(Animal):
#     def bark(self):
#         print("Dog will bark")

# D1=Dog()
# D1.eat()
# D1.sleep()
# D1.bark()

# 
#Create Person → Student.
# class Person:
#     def __init__(self,n,a):
#         self.n=n
#         self.a=a
        
#     def name(self):
#         print(f"Person's name is {self.n}")

#     def age(self):
#         print(f"Person's age is {self.a}")

# class Student(Person):
#     def __init__(self, n, a,ID):
#         super().__init__(n, a)
#         self.ID=ID
#     def id(self):
#         print(f"Student ID is {self.ID}")

# S1=Student("Zahid",21,205)
# S1.name()
# S1.age()
# S1.id()

#Create Employee → Manager.
class Employee:
    