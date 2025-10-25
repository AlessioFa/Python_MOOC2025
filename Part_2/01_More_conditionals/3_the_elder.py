"""
Please write a program which asks for the names and ages of two persons. The program should then print out the name of the elder.

Some examples of expected behaviour:

Person 1:
Name: Alan
Age: 26
Person 2:
Name: Ada
Age: 27
The elder is Ada

Person 1:
Name: Bill
Age: 1
Person 2:
Name: Jean
Age: 1
Bill and Jean are the same age
"""


def age_check() -> str:
    first_p: str = input("Enter the first person name: ").capitalize()
    second_p: str = input("Enter the second person name: ").capitalize()

    first_p_age: int = int(input("Enter the age of the first person: "))
    second_p_age: int = int(input("Enter the age of the second person: "))

    print(f"Person 1:\nName: {first_p}")
    print(f"Age: {first_p_age}")
    
    print(f"Person 2:\nName: {second_p}")
    print(f"Age: {second_p_age}")

    if first_p_age > second_p_age:
        print(f"The elder is {first_p}")
    
    elif second_p_age > first_p_age:
        print(f"The elder is: {second_p}")
    
    else:
        print(f"{first_p} and {second_p} are the same age")


age_check()
