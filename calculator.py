def additiion(num1, num2):
    #take two integers and add them together.
    return num1 + num2

print ("Calculator!")
num1 = int(input ("Input an integer: "))
num2 = int(input ("Input another integer: "))
operator = input ("What to do with them?: ")

if operator == "+":
    print (additiion(num1, num2))
