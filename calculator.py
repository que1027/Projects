print("Welcome To The Best Calculator Ever!")
print('')
print("Please Enter Your First Number: ")
firstNum = input()
print("Please Enter Your Operator: ")
operation = input()
print("Please Enter Your Second Number: ")
secondNum = input()




if operation == "+":
    print(firstNum + " + " + secondNum + " =")
    print(float(firstNum) + float(secondNum))
elif operation == "-":
    print(firstNum + " - " + secondNum + " =")
    print(float(firstNum) - float(secondNum))
elif operation == "*":
    print(firstNum + " * " + secondNum + " =")
    print(float(firstNum) * float(secondNum))
elif operation == "/":
    print(firstNum + " / " + secondNum + " =")
    print(float(firstNum) / float(secondNum))
else:
    print("Please Enter A Valid Operator")

