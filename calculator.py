def additiion(num1, num2):
    #take two integers and add them together.
    return num1 + num2

def subtraction(numOne, numTwo):
    #take two integers and subtract the second from the first.
    return num1 + num2

def multiplication(numOne, numTwo):
    #blah
    return num1 * num2

def division(numOne, numTwo):
    #bleh
    return num1 / num2

print ("Calculator!")

while True:
    print ("Enter q to exit.")

    NUM1 = input ("Input an integer: ")
    if NUM1 == "q":
        break
    NUM2 = input ("Input another integer: ")
    if NUM2 == "q":
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