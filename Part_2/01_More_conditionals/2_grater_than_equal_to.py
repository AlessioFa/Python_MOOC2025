"""
Please write a program which asks for two integer numbers. The program should then print out whichever is greater. If the numbers are equal, the program should print a different message.

Some examples of expected behaviour:
Sample output

Please type in the first number: 5
Please type in another number: 3
The greater number was: 5

Please type in the first number: 5
Please type in another number: 8
The greater number was: 8

Please type in the first number: 5
Please type in another number: 5
The numbers are equal!
"""


def number_check():
    first_num: int = int(input("Please type in the first number: "))
    second_num: int = int(input("Please type another number: "))

    if first_num > second_num:
        print(f"The greater number was: {first_num}")

    elif second_num > first_num:
        print(f"The greater number was: {second_num}")

    else:
        print("The numbers are equal!")


number_check()
