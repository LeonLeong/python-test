import random
import re

def weakRegex(length: int):
    #password with upper and lower case alphabets
    #test
    #test2
    #test3
    return

def moderateRegex(length: int):
    #password with upper and lower case alphabets
    #+numbers
    return

def strongRegex(length: int):
    #password with upper and lower case alphabets
    #+numbers
    #+special characters.
    return

def main():
    #Loop to get user input, will not break unless the requirements
    #of both inputs are satisfied.
    while True:
        num1 = int(input("Choose password strength:\n1 = Weak\n2 = Moderate\n3 = Strong\nStrength: "))
        num2 = int(input("Choose password length[6-12]: "))
        if (1 <= num1 <= 3 and 6 <= num2 <= 12):
            break
        else:
            print("User input error. Please try again.")

    if(num1 == 1):
        print("Generating password with weak regex...")
        weakRegex(num2)
    elif(num1 == 2):
        print("Generating password with moderate regex...")
        moderateRegex(num2)
    elif(num1 == 3):
        print("Generating password with strong regex...")
        strongRegex(num2)

if __name__ == "__main__":
    main()