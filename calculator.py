def additiion(num1, num2):
    #take two integers and add them together.
    return num1 + num2

def subtraction(num1, num2):
    #take two integers and subtract the second from the first.
    return num1 + num2

def multiplication(num1, num2):
    #blah
    return num1 * num2

def division(num1, num2):
    #bleh
    return num1 / num2

print ("Calculator!")

while True:
    print ("Enter q to exit.")

    num1 = input ("Input an integer: ")
    if num1 == "q":
        break
    num2 = input ("Input another integer: ")
    if num2 == "q":
        break

    if (num1 != None or num2 != None):
        #lazy to implement regex for now.
        num1 = float(num1)
        num2 = float(num2)

    operator = input ("What to do with them? (+, -, *, /): ")
    if operator == "+":
        print (additiion(num1, num2))
    elif operator == "-":
        print (subtraction(num1, num2))
    elif operator == "*":
        print (multiplication(num1, num2))
    elif operator == "/":
        print (division(num1,num2))
    else:
        print ("Command not recognized.")

print("Goodbye!")