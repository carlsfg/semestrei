
print (30 * '-')
print ("Welcome to the Python Calculator")
print (30 * '-')
print ("Please, choose from one of the following: ")
print ("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Power to\n6. Convert Farenheit to Celcuis\n7. Calculate the sale tax\n8. Calculate the income tax\n9. Exit")
    
def main():
    print ("Select:\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Power to\n6. Convert Farenheit to Celcuis\n7. Calculate the sale tax\n8. Calculate the income tax\n9. Exit")
    x = input()

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

elif calc_function == 9:
    print ("Goodbye")
    exit()
    
else:
    print "**Select a number from the selection**"


answer = raw_input("Do you want to run the calculator again? (y/n): ")
if answer not in ('y', 'n'):
    print("Invalid input. Goodbye")
    exit()
elif answer == 'y':
    main()
else:
    print("Goodbye")
    exit()