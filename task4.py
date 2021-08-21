#task4
num1 = float(input("Enter your first number : "))
num2 = float(input("Enter your second number : "))
operator = input("please Enter your operator : ")

if operator == "+":
 print (num1 + num2)
elif operator == "-":
 print (num1 - num2)
elif operator == "/":
 print (num1 / num2)
elif operator == "*":
 print (num1 * num2)
else:
 print("please enter correct operator")
