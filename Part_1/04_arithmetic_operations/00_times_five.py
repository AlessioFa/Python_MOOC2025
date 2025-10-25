"""
Please write a program which asks the user for a number. The program then prints out the number multiplied by five.

The program should function as follows:
Sample output

Please type in a number: 3
3 times 5 is 15
"""

user_number: int = int(input("Enter a number: "))

print(f"{user_number} times 5 is {user_number * 5}")
