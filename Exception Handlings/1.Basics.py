#Write a program that handles a ZeroDivisionError when dividing two numbers.
try:
    num=int(input("Entar a number:"))
    Div=100/num
    print(f"Division:{Div}")
except ZeroDivisionError:
    print("Number cannot divide by zeor")

#Take two numbers from the user and handle ValueError if the user enters non-numeric input.
try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print(f"Sum of two numbesr:{num1+num2}")
except ValueError:
    print("Enter a proper number")

#Write a program using try and except to convert a string into an integer.
try:
    str=input("Enter a string:")
    num=int(str)
    print(f"Conversion from String to Integer:{num}")
except:
    print("Enter a proper string")

#Handle an error when accessing an invalid index of a list.
try:
    lst=[10,20,30,40,50]
    print(lst[9])
except IndexError:
    print("Your index is out of range")

#Handle an error when accessing a key that doesn't exist in a dictionary.
try:
    Student={"Name":"Zahid","Age":21,"Marks":200}
    print(Student["Age"])
except KeyError:
    print("Key is not present in the Dictionary")

#Handle TypeError when trying to add an integer and a string.
try:
    num=int(input("Enter a number:"))
    print(f"Sum of Digits are:{"X"+num}")
except TypeError:
    print("String cannot be added to integer")

#Write a program that safely converts user input into a float.
try:
    num=int(input("Enter a number:"))
    a=float(num)
    print(f"Number is converted to float:{a}")
except:
    print("Enter a proper number")

#Handle NameError when trying to use an undefined variable.
try:
    name="Zahid Khan"
    print(name)
except:
    print("varialbe is nor defineed")