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
class Employee:
    def __init__(self,salary:int):
        self.sal=salary
        
    

    @property
    def sal(self):
        return self.__salary

    @sal.setter
    def sal(self,Salary):
        if Salary>=0:
            self.__salary=Salary
        else:
            self.__salary=0
            print("Salary should not b negative")

E1=Employee(-1000)
E1.sal
print(E1.sal)

#Create a PasswordManager with a private password.
class PasswordManager:
    def __init__(self,Password):
        self.__Password=Password

    @property
    def password(self):
        return self.__Password

U1=PasswordManager(2223)
print(U1.password)

#Create a User class where email can only be changed through a method.
class User:
    def __init__(self,name,email):
        self.name=name
        self.__email=email

    @property
    def display_email(self):
        return self.__email

    def change_email(self,new_email):
        self.__email=new_email

U1=User("Zahid","Khanzahid2223@gmail.com")
print(U1.display_email)
U1.change_email("pathan123@gmail.com")
print(U1.display_email)

#Create a Product class where price cannot be negative.
class Product:
    def __init__(self,prodect_name:str,price:int):
        self.prodect_name=prodect_name
        self.__price=price

    
    def amount(self):
        if self.__price>=0:
            return self.__price
        else:
            return "Invalid Price"

P1=Product("Mobile",-90000)
print(P1.amount())


#Create a Wallet class with private balance.
class Wallet:
    def __init__(self,balance):
        self.__balance=balance


    @property
    def balance(self):
        return self.__balance

p1=Wallet(100000)
print(p1.balance)

#Create a Person class where age cannot be negative.
class Person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.__age=age


    def nam(self):
        return self.name


    @property
    def info(self):
        if self.__age>=0:
            return self.__age
        else:
            return "Invalid Age"

P1=Person("Zahid",21)
print(P1.nam())
print(P1.info)
    

#Create a BankAccount where withdrawal cannot exceed balance.
class BankAccount:
    Balance=20000
    def __init__(self,withdraw):
        self.withraw=withdraw

    @property
    def withdrawal(self):
        if self.withraw<=self.Balance:
            Bal=self.Balance-self.withraw
            print(f"Current Balance:{Bal}")
            return "Withdraw Successful!"
        else:
            return "Innsufficient Balance"


P1=BankAccount(20000)
print(P1.withdrawal)

