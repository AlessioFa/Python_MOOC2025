"""
Python comparison operators can also be used on strings. String a is smaller than string b if it comes alphabetically before b. Notice however that the comparison is only reliable if

    the characters compared are of the same case, i.e. both UPPERCASE or both lowercase
    only the standard English alphabet of a to z, or A to Z, is used.

Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

You can assume all words will be typed in lowercase entirely.

Some examples of expected behaviour:

Please type in the 1st word: car
Please type in the 2nd word: scooter
scooter comes alphabetically last.

Please type in the 1st word: zorro
Please type in the 2nd word: batman
zorro comes alphabetically last.

Please type in the 1st word: python
Please type in the 2nd word: python
You gave the same word twice.
"""

def first_letter_checker() -> str:
    first_word: str = input("Please type in the 1st word: ")
    second_word: str = input("Please type in the 2nd word: ")

    if first_word == second_word:
        print("You gave the same word twice.")
    
    elif first_word > second_word:
        print(f"{first_word} comes alphabetically first.")

    else:
        print(f"{second_word} comes alphabetically last.")


first_letter_checker()
