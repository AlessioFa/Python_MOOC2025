# Write your solution here
f_temp = int(input("Please type in a temperature (F): "))
c_temp = (f_temp - 32) * 5 / 9

if f_temp < 0:
    print(f"{f_temp} degrees Fahrenheit equals to {c_temp} degrees Celsius\nBrr! It's cold in here!")
else:
    print(f"{f_temp} degrees Fahrenheit equals to {c_temp} degrees Celsius")
