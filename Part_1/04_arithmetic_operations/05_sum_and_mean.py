"""
Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.

The program should function as follows:

Number 1: 2
Number 2: 1
Number 3: 6
Number 4: 7
The sum of the numbers is 16 and the mean is 4.0
"""

user_first_number: int = int(input("Enter the first number: "))
user_second_number: int = int(input("Enter the first number: "))
user_third_number: int = int(input("Enter the first number: "))
user_fourth_number: int = int(input("Enter the first number: "))

print(f"Number 1: {user_first_number}\nNumber 2: {user_second_number}\nNumber 3: {user_third_number}\nNumber 4: {user_fourth_number}")

print(f"The sum of the numbers is {user_first_number + user_second_number + user_third_number + user_fourth_number} and the mean is {(user_first_number + user_second_number + user_third_number + user_fourth_number) / 4}")
