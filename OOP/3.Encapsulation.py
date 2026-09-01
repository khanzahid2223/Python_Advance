"""
Create a PasswordManager with a private password.
Create a User class where email can only be changed through a method.
Create a Product class where price cannot be negative.
Create a Wallet class with private balance.
Create a Person class where age cannot be negative.
Create a BankAccount where withdrawal cannot exceed balance.
Create a Mobile class with a private battery percentage.
Create a LoginSystem with private username and password.
Challenge: Design a secure ATM class using encapsulation
"""

#Create a class with a private variable.
class Bank:
    def __init__(self,name:str,balance:int):
        self.name=name
        self.__balance=balance

P1=Bank("Zahid",90900)
print(P1.self.__Balance)

#Create a BankAccount where balance cannot be directly modified.
class BankAccount:
    def __init__(self,name:str,balance:int):
        self.name=name
        self.__balance=balance

    def bal(self):
        return self.__balance

P1=BankAccount("Zahid",1000)
print(P1.bal())

#Create getter and setter methods for age.
class Person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.__age=age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        self.__age=value


P1=Person("Zahid",21)
print(P1.age)
P1.age=60
print(P1.age)

#Create a Student class where marks must remain between 0 and 100.
class Student:
    def __init__(self,name:str,marks:int):
        self.name=name
        self.__marks=0
        self.marks=marks

    @property
    def marks(self):
        return self.__marks
    

    @marks.setter
    def marks(self,new_marks):
        if 0<=new_marks<=100:
            self.__marks=new_marks
            print("Marks stroed successfully!")
        else:
            print("Rejected due to invalid marks")
            

S1=Student("Zahid",99)
S1.marks
print(f"Marks:{S1.marks}")

#Create an Employee class with private salary.
class Employee:
    def __init__(self,salary:int):
        self.__salary=salary

    @property
    def sal(self):
        return self.__salary

    @sal.setter
    def sal(self,new_salary):
        self.__salary=new_salary
        

E1=Employee(10000)
print(E1.sal)
E1.sal=2000
print(E1.sal)

#Prevent negative salary using encapsulation.
hello