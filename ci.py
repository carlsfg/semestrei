print("Type integer numbers to get the average. Input a negative to exit.")

count = 0
number = 0
sum = 0
avg = 0

while number >= 0:
    number = int(input())
    if number >= 0:
        sum = sum + number
        count = count + 1
    else:
        avg = sum / count
        print ("_" * 30)
        print "Average:", avg
        print "Sum is:", sum
        print "Count is:", count