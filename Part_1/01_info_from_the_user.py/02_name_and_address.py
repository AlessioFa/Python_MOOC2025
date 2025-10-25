"""
Please write a program which asks for the user's name and address. The program should also print out the given information, as follows:

Given name: Steve
Family name: Sanders
Street address: 91 Station Road
City and postal code: London EC05 6AW
Steve Sanders
91 Station Road
London EC05 6AW
"""

name: str = input("Enter your name: ").title()
family_name: str = input("Enter the name of your family: ").title()
street_address = input("Enter your street address: ")
city_postal_code = input("Enter your city and postal code: ")

print(name + " " + family_name)
print(street_address)
print(city_postal_code)
