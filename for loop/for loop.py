# Take input from user.
num = int(input("Print sum of even numbers till : "))

total = 0

for i in range(10, num + 1):

    # Check for even or not.
    if((i % 2) == 0):
        total = total + i

print("\nSum of even numbers from 10 to", num, "is :", total)
 # Take input from user.
num = int(input("Print sum of 0dd numbers till : "))

total = 0

for i in range(10, num + 1):

    # Check for odd or not.
    if (not(i % 2) == 0):
        total = total + i

print("\nSum of odd numbers from 10 to", num, "is :", total)

# Take input from user
num = int(input("Print all odd numbers till : "))

print("\nOdd numbers from 1 to", num, "are : ")

for i in range(1, num + 1):

    #Check for odd or not.
    if((i % 2) != 0):
        print(i, end=" ")# Take input from user
num = int(input("Print all odd numbers till : "))

print("\nOdd numbers from 1 to", num, "are : ")

for i in range(1, num + 1):

    #Check for odd or not.
    if((i % 2) ==0):
        print(i, end=" ")

        # Take input from user
upto = int(input("Find prime numbers upto : "))

print("\nAll prime numbers upto", upto, "are : ")

for num in range(2, upto + 1):

    i = 2

    for i in range(2, num):
        if(num % i == 0):
            i = num
            break;

    # If the number is prime then print it.
    if(i != num):
        print(num, end=" ")

# Take input from user
upto = int(input("Find sum of prime numbers upto : "))

sum = 0

for num in range(2, upto + 1):

    i = 2
    
    for i in range(2, num):
        if (int(num % i) == 0):
            i = num
            break;

    #If the number is prime then add it.
    if i is not num:
        sum += num

print("\nSum of all prime numbers upto", upto, ":", sum)2