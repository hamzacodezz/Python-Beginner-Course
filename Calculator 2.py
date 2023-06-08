num1=float(input("Enter first number: "))
op=input("Enter operator (x / + - ): ")
num2=float(input("Enter secomd number: "))

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="x":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("invalid operation")