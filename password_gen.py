import random
import re

def weak_regex(length: int):
    #password with upper and lower case alphabets
    return

def moderate_regex(length: int):
    """
    password with upper and lower case alphabets
    +numbers
    """
    return

def strong_regex(length: int):
    """
    password with upper and lower case alphabets+numbers+special characters.
    """
    return

def main():
    """
    Loop to get user input, will not break unless the requirements
    of both inputs are satisfied.
    """
    while True:
        num1 = int(input("""Choose password strength:
        \n1 = Weak
        \n2 = Moderate
        \n3 = Strong
        \nStrength: """))
        num2 = int(input("Choose password length[6-12]: "))
        if (1 <= num1 <= 3 and 6 <= num2 <= 12):
            break
        else:
            print("User input error. Please try again.")

    if(num1 == 1):
        print("Generating password with weak regex...")
        weak_regex(num2)
    elif(num1 == 2):
        print("Generating password with moderate regex...")
        moderate_regex(num2)
    elif(num1 == 3):
        print("Generating password with strong regex...")
        strong_regex(num2)

if __name__ == "__main__":
    main()