"""
Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.

The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.

Some examples of expected behaviour:
Sample output

What is the weather forecast for tomorrow?
Temperature: 21
Will it rain (yes/no): no
Wear jeans and a T-shirt
Sample output

What is the weather forecast for tomorrow?
Temperature: 11
Will it rain (yes/no): no
Wear jeans and a T-shirt
I recommend a jumper as well
Sample output

What is the weather forecast for tomorrow?
Temperature: 7
Will it rain (yes/no): no
Wear jeans and a T-shirt
I recommend a jumper as well
Take a jacket with you
Sample output

What is the weather forecast for tomorrow?
Temperature: 3
Will it rain (yes/no): yes
Wear jeans and a T-shirt
I recommend a jumper as well
Take a jacket with you
Make it a warm coat, actually
I think gloves are in order
Don't forget your umbrella!
"""

"""def what_to_wear():
    temp: int = int(input())
    rain: str = input().lower()

    if temp == 20:
        print("I recommend a jumper as well")
        return

    if temp > 20:
        print("Wear jeans and a T-shirt")

    elif 11 <= temp <= 19:
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")

    elif 6 <= temp <= 10:
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")

    else:
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
        print("Make it a warm coat, actually")
        print("I think gloves are in order")

    if rain == "yes":
        print("Don't forget your umbrella!")

what_to_wear()"""


# SECONDA VERSIONE 

def what_to_wear2():
    temp: int = int(input("Tomorrow's temp: "))
    rain: str = input("Will it rain tomorrow? (yes/no): ").lower()

    # Lista per accumulare i consigli
    clothes = []

    # Consigli base in base alla temperatura
    if temp > 20:
        clothes.append("Wear jeans and a T-shirt")
    elif 11 <= temp <= 20:
        clothes.append("Wear jeans and a T-shirt")
        clothes.append("I recommend a jumper as well")
    elif 6 <= temp <= 10:
        clothes.append("Wear jeans and a T-shirt")
        clothes.append("I recommend a jumper as well")
        clothes.append("Take a jacket with you")
    else:  # temp <= 5
        clothes.append("Wear jeans and a T-shirt")
        clothes.append("I recommend a jumper as well")
        clothes.append("Take a jacket with you")
        clothes.append("Make it a warm coat, actually")
        clothes.append("I think gloves are in order")

    # Consiglio per la pioggia
    if rain == "yes":
        clothes.append("Don't forget your umbrella!")

    # Stampa tutti i consigli
    for advice in clothes:
        print(advice)

what_to_wear2()
