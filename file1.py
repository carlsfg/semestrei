#This script will be a calculator with different funtions
print (30 * '-')
print ("Welcome to the Python Calculator")
print (30 * '-')
print ("Please, choose from one of the following: ")
print ("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Power to\n6. Convert Farenheit to Celcuis\n7. Calculate the sale tax\n8. Calculate the income tax")
print (30 * '=')
calc_function = (input("Enter your selection: "))

if calc_function == 1:
    print "Hello, World"

elif calc_function == 2:
    print "Hello, World"

elif calc_function == 3:
    print "Hello, World"

elif calc_function == 4:
    print "Hello, World"

elif calc_function == 5:
    print "Hello, World"

elif calc_function == 6:
    print "Hello, World"

elif calc_function == 7:
    print "Hello, World"

elif calc_function == 8:
    print "Hello, World"

else:
    print "Select a number from the selection"
    print "The program will now terminate."

num =0
while num< 5:
    num = num + 1
    print("num =", num)
