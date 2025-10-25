"""
Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

You may assume the letters will be either all uppercase, or all lowercase.

Some examples of expected behaviour:

1st letter: x
2nd letter: c
3rd letter: p
The letter in the middle is p

1st letter: C
2nd letter: B
3rd letter: A
The letter in the middle is B
"""


def alphabetically_in_the_middle():

    i = 0
    letters = []

    while i < 3:
        user_letter = input("Enter three letters: ")

        i += 1

        letters.append(user_letter)
    
    print(letters)

    letters.sort()

    print(f"The letter in the middle is {letters[1]}")
        

alphabetically_in_the_middle()
