"""
This program already contains two integer variables, x and y:

x = 27
y = 15

Please complete the program so that it also prints out the following:

27 + 15 = 42
27 - 15 = 12
27 * 15 = 405
27 / 15 = 1.8

The program should work correctly even if the values of the variables are changed. That is, if the first two lines are replaced with this

x = 4
y = 9

the program should print out the following:

4 + 9 = 13
4 - 9 = -5
4 * 9 = 36
4 / 9 = 0.4444444444444444
"""

x = 27
y = 15

num_sum: int = x + y
num_subtraction: int = x - y
num_moltiplication: int = x * y
num_division: float = x / y

print(f"{x} + {y} = {num_sum}")
print(f"{x} - {y} = {num_subtraction}")
print(f"{x} * {y} = {num_moltiplication}")
print(f"{x} / {y} = {num_division}")
