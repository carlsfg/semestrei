#@Author: Carlos Flores
#@Matricula: A01206352
#@Version: 1.0
#@Date: 13/03/19

#This Python script is a calculator that can add, subtract, multiply, divide, convert celcius to farenheit, calculate the income tax and the sales tax.

#This function is for adding two numbers
def add():
    x = input ("Type number 1: ")
    y = input ("Type number 2: ")
    print ("The result is:"), x + y

#This function is for substracting two numbers
def subtract():
    x = input ("Type number 1: ")
    y = input ("Type number 2: ")
    print ("The result is:"), x - y

#This function is for multiplying two numbers
def multiply():
    x = input ("Type number 1: ")
    y = input ("Type number 2: ")
    print ("The result is:"), x * y

#This function is for dividing two numbers
def divide():
    x = input ("Type number 1: ")
    y = input ("Type number 2: ")
    print ("The result is:"), x / y

#This function is to elevate a number to the power of a number
def power():
    x = input ("Type base number: ")
    y = input ("Type power number: ")
    print ("The result is:"), x ** y

#This function is to convert Farenheit to Celsius
def convert():
    x = input ("Type temperature in Farentheit: ")
    print (x - 32) * 5 / 9

#This function is to calculate the sales tax
def salesTax():
    x = float (input ("Type subtotal: $"))
    y = float (input ("Type tax in %: "))
    tax = x * (y/100)
    print ("Tax is: $"), tax
    print ("Total price is: $"), x + tax

#This function is to calculate the income tax
def incomeTax():
    x = input ("Type anual income: $")
    y = input ("Type anual outcome: $")
    if y > x:
        print "You don't have to pay taxes."
    else:
        (x-y)*.3

#Menu
print (30 * '-')
print ("Welcome to the Python Calculator")
print (30 * '-')

#Options
print ("Please, choose from one of the following: ")
print ("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Power to\n6. Convert Farenheit to Celcuis\n7. Calculate the sale tax\n8. Calculate the income tax\n9. Exit")
selection = input("Insert option:")
    
if selection == 1:
    add()

if selection == 2:
    subtract()

if selection == 3:
    multiply()

if selection == 4:
    divide()

if selection == 5:
    power()

if selection == 6:
    convert()

if selection == 7:
    salesTax()

if selection == 8:
    incomeTax()

if selection == 9:
    print ("Goodbye")
    exit()

