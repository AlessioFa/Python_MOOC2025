"""Please write a program which asks the user for an integer number. The program should then print out the magnitude of the number according to the following examples.
Sample output

Please type in a number: 950
This number is smaller than 1000
Thank you!
Sample output

Please type in a number: 59
This number is smaller than 1000
This number is smaller than 100
Thank you!
Sample output

Please type in a number: 2
This number is smaller than 1000
This number is smaller than 100
This number is smaller than 10
Thank you!
Sample output

Please type in a number: 1123
Thank you!"""


user_number: int = int(input("Please type in a number: "))


if user_number < 10:
    print("This number is smaller than 1000\nThis number is smaller than 100\nThis number is smaller than 10\nThank you!")

elif user_number < 100:

    print("This number is smaller than 1000\nThis number is smaller than 100\nThank you!")

else:

    print("This number is smaller than 1000\nThank you!")


if user_number < 1000:
    print("This number is smaller than 1000")

if user_number < 100:
    print("This number is smaller than 100")

if user_number < 10:
    print("This number is smaller than 10")

print("Thank you!")