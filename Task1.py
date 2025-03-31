num1=input("Enter the first number: ")
num2=input("Enter the second number: ")
if not num1.isdigit():
    print("first number is not a valid number")

if not num2.isdigit():
    print("second number is not a valid number")
if (num1.isdigit() and  num2.isdigit()):
    out=int(num1)+ int(num2)
    print("Addition: "+ str(out) )
    out=int(num1)- int(num2)
    print("Subtraction: "+ str(out) )
    out=int(num1)* int(num2)
    print("Multiplication: "+ str(out) )
    out=int(num1)/ int(num2)
    print("Division: "+ str(out) )
