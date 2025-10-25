"""Please write a program which asks for the user's name. If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. The price of a single portion is 5.90.

Two examples of the program's execution:
Sample output

Please tell me your name: Kramer
How many portions of soup? 2
The total cost is 11.8
Next please!
Sample output

Please tell me your name: Jerry
Next please!
"""

one_soup_price: float = 5.90
user_name: str = input("Please tell me your name: ")

if user_name != "Jerry".lower():
    soup_portions: int = int(input("How many portions of soup? "))
    print(f"The total cost is {soup_portions * one_soup_price}")
else:
    print("Next please!")




# same exercise with the use of while and raise error
price_one_soup: float = 5.90

while True:
    name: str = input("Please tell me your name: ")
    
    if name == "stop":
            break  
    
    if name != "Jerry":
        portions: int = int(input("How many portions of soup? "))
        print(f"The total cost is {portions * price_one_soup:.2f}")
    else:
        print("Next please!")
