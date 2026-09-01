#Create a class using __init__().
class Sample:
    def __init__(self):
        print("Hello Developer")

S1=Sample()

#Create a class with multiple constructor parameters.
class Student:
    def __init__(self,name:str,age:int,gender:str):
        self.name=name
        self.age=age
        self.gender=gender

    def display(self):
        print(f"My name is {self.name}, My age is {self.age} and My gender is {self.gender}")

S1=Student("Zahid",21,"Male")
S1.display()

#Create a Student class with a method to display details.
class Student:
    def __init__(self,name:str,age:int,gender:str):
        self.name=name
        self.age=age
        self.gender=gender

    def display(self):
        print(f"My name is {self.name}, My age is {self.age} and My gender is {self.gender}")

S1=Student("Zahid",21,"Male")
S1.display()

#Create a Calculator class with add, subtract, multiply and divide methods.
class Calculator:
    def __init__(self,num1:int,num2:int)->None:
        self.num1=num1
        self.num2=num2

    def add(self):
        print(f"Addition:{self.num1+self.num2}")

    def sub(self):
        print(f"Subtraction:{self.num1-self.num2}")

    def mul(self):
        print(f"Multiplication:{self.num1*self.num2}")

    def div(self):
        print(f"Division:{self.num1%self.num2}")

Cal=Calculator(100,50)
Cal.add()
Cal.sub()
Cal.mul()
Cal.div()

#Create a BankAccount with deposit and withdraw methods
class BankAccount:
    Balance=100000
    def deposit(self,amount:int):
        self.amount=amount
        print(f"Current Balance after deposit:{self.Balance+self.amount}")

    def withdraw(self,amount:int):
        self.amount=amount
        print(f"Available balance after withdraw :{self.Balance-self.amount}")

B1=BankAccount()
B1.deposit(20000)
B1.withdraw(15000)

#Create a ShoppingCart class with add_item() and remove_item().
class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add_item(self,*products):
        self.items.extend(products)
        print(self.items)

    def remove_item(self,product):
        self.items.remove(product)
        print(self.items)

S1=ShoppingCart()
S1.add_item("Laptop","Mobile","Charger","Keyboard","Mouse","Adapter")
S1.remove_item("Laptop")

#Create a LibraryBook class with borrow() and return_book().
class LibraryBook:
    def __init__(self,title:str,author:str,is_barrowed:bool=False):
        self.title=title
        self.author=author
        self.is_barrowed=is_barrowed

    def barrowed(self):
        if self.is_barrowed == True:
            print("Aleady Barrowed")
        else:
            self.is_barrowed=True
            print("Successful")

    def return_book(self):
        if self.is_barrowed==True:
            self.is_barrowed=False
            print("Book has returned succefully")
        else:
            print("Not Barrowed")

B1=LibraryBook("Python","Zahid",False)
B1.barrowed()
B1.return_book()

#Create a VotingSystem class that checks whether a person can vote.
class VotingSystem:
    def __init__(self,age:int):
        self.age=age

    def Vote(self):
        if self.age>=18:
            print("Valid to vote")
        else:
            print("Your are not 18+")

V1=VotingSystem(29)
V1.Vote()

#Create a Result class that calculates pass/fail.
class Result:
    def __init__(self,student_name:str,marks:list[int]):
        self.student_name=student_name
        self.marks=marks

    def check_result(self):
        total=0
        for num in self.marks:
            total=total+num
        print(total)
        if total>=35:
            print("Pass")
        else:
            print("Fail")

S1=Result("Zahid",[9,3,6,7])
S1.check_result()

#Create a Login class that validates username and password.
class Login:
    username="Zahid"
    password=2223
    def __init__(self,uname,passw):
        self.uname=uname
        self.passw=passw

    def verify(self):
        if self.uname==self.username and self.passw==self.password:
            print("Login Successful!")
        else:
            print("Invalid Username or Password")

U1=Login("Zahid",2223)
U1.verify()

#Create a HotelRoom class with booking and cancellation methods.
class HotelRoom:
   
    def __init__(self, Room_No=205,Room_Type="single",Price=3000,is_booked:bool=False):
        self.Room_No=Room_No
        self.Room_Type=Room_Type
        self.Price=Price
        self.is_booked=is_booked

    def booking(self):
        if self.is_booked==False:
            print("Room is Available")
            self.is_booked=True
        else:
            print("Room is already booked")

    def cancellation(self):
        if self.is_booked==True:
            print("Cancalation Successful!")
            self.is_booked=False
        else:
            print("Room is not booked")

R1=HotelRoom()
R1.booking()
R1.cancellation()