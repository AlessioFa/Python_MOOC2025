"""Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.

Some examples of expected behaviour:
Sample output

Number 1: 10
Number 2: 17
Operation: add

10 + 17 = 27
Sample output

Number 1: 4
Number 2: 6
Operation: multiply

4 * 6 = 24
Sample output

Number 1: 4
Number 2: 6
Operation: subtract

4 - 6 = -2"""


user_number_1: int = int(input("Number 1: ")) 

user_number_2: int = int(input("Number 2: "))

user_operation = input("Enter a valid operation (add / subtract / multiply): ")

if not user_operation:
    print()

else:
    if user_operation == "add":

        print("Operation: add\n")
        print(f"{user_number_1} + {user_number_2} = {user_number_1 + user_number_2}")
    
    elif user_operation == "subtract":

        print("Operation: subtract\n")
        print(f"{user_number_1} - {user_number_2} = {user_number_1 - user_number_2}")
    
    elif user_operation == "multiply":

        print("Operation: multiply")
        print(f"{user_number_1} * {user_number_2} = {user_number_1 * user_number_2}")
    
