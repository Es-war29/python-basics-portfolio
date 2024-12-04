
# Calculator App
operator = input("Enter operator +,-,*,/,% : ")
n1 = float(input("Enter number1:"))
n2 = float(input("Enter number2:"))

if operator == "+":
    result = n1+n2
    print(round(result,2))
elif operator == "-":
    result = n1-n2
    print(round(result,2))
elif operator == "*":
    result = n1*n2
    print(round(result, 2))
elif operator == "/":
    result = n1/n2
    print(round(result,2))
elif operator == "%":
    result = n1%n2
    print(round(result,2))
else:
    print(f"invalid {operator}")

