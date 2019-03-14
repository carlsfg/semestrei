#@Author: Carlos Flores
#@Matricula: A01206352
#@Version: 1.0
#@Date: 13/03/19

#This Python script is a calculator that can: 
#add, subtract, multiply, divide, 
#convert celcius to farenheit, calculate the income tax and the sales tax.

#This function is for adding two numbers
def add():
    x = float (input ("Type number 1: "))
    y = float (input ("Type number 2: "))
    print ("The result is:"), x + y

#This function is for substracting two numbers
def subtract():
    x = float (input ("Type number 1: "))
    y = float (input ("Type number 2: "))
    print ("The result is:"), x - y

#This function is for multiplying two numbers
def multiply():
    x = float (input ("Type number 1: "))
    y = float (input ("Type number 2: "))
    print ("The result is:"), x * y

#This function is for dividing two numbers
def divide():
    x = float (input ("Type number 1: "))
    y = float (input ("Type number 2: "))
    print ("The result is:"), x / y

#This function is to elevate a number to the power of a number
def power():
    x = float (input ("Type base number: "))
    y = float (input ("Type power number: "))
    print ("The result is:"), x ** y

#This function is to convert Farenheit to Celsius
def convert():
    x = int (input ("Type temperature in Farentheit: "))
    print ("The temperature in Celsius is :"), (x - 32) * 5 / 9

#This function is to calculate the sales tax
def salesTax():
    x = float (input ("Type subtotal: $"))
    y = float (input ("Type tax in %: "))
    tax = x * (y/100)
    print ("Tax is: $"), tax
    print ("Total price is: $"), x + tax

#This function is to calculate the income tax
def incomeTax():
    x = float (input("Type anual income: $"))
    y = float (input("Type anual outcome: $"))
    z = float (input("Type the tax rate in: %"))
    if y > x:
        print "You don't have to pay taxes."
    if x > y:
        taxToPay=(x-y)*(z/100)
        print "Your tax pay is: $", taxToPay

#Options
def main():
    print ("Please, choose from one of the following: ")
    print (40 * '-')
    print ("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Power to\n6. Convert Farenheit to Celcuis\n7. Calculate the sale tax\n8. Calculate the income tax\n9. Exit")
    print ("\n")
    selection = input("Type number option:")
    
    #Conditionals
    if selection == 1:
        add()

    elif selection == 2:
        subtract()

    elif selection == 3:
        multiply()

    elif selection == 4:
        divide()

    elif selection == 5:
        power()

    elif selection == 6:
        convert()

    elif selection == 7:
        salesTax()

    elif selection == 8:
        incomeTax()

    elif selection == 9:
        print ("Goodbye")
        exit()
    
    else:
        print ("Please type a valid option")

    #This section is to return to use if user wants to   
    
    start = raw_input("Do you want to run the calculator again? (y/n): ")
    if start not in ('y', 'n'):
        print("Invalid input. Sorry")
        exit()
    elif start == 'y':
        main()
    elif start == 'n':
        print("Goodbye")
        exit()
    else:
        print("Invalid input. Sorry")
        exit()

#Menu
print (50 * '-')
print ("W E L C O M E  T O  T H E  P Y T H O N  C A L C U L A T O R")
print (50 * '-')
main()

