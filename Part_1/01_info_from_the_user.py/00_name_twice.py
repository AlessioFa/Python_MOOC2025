"""
Please write a program which asks for the user's name and then prints it twice, on two consecutive lines.

An example of the how the program should function:

What is your name? Paul
Paul
Paul
"""

name: str = input("Enter your name:").title()

print(f"\n{name}\n{name}")
