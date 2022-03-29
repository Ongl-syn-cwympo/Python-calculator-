# Program; make a program simple calculator for all functions (# This version 2 is more efficient and takes less lines of code.)
# Program can only handle 2 inputs
# Python code 
# Created by Ongl syn cwympo 
# https://github.com/Ongl-syn-cwympo

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))

if sign == "+":
  print("+ Addition calculator +")
  answer = int(num1) + int(num2) # This function adds both numbers inputed together
  
  print("The solution is: ", + answer) # This outputs the combined numbers
  
if sign == "-":
  print("- Subtraction calculator -")
  answer = int(num1) - int(num2) # This function subs both numbers inputed together
  
  print("The solution is: ", + answer) # This outputs the subtracted numbers
  
if sign == "*":
  print("* Multiplication calculator *")
  answer = int(num1) * int(num2) # This function multiplies both numbers inputed together
  
  print("The solution is: ", + answer) # This outputs the multiplied numbers
  
if sign == "/":
  print("/ Division calculator /")
  answer = int(num1) / int(num2) # This function divides both numbers inputed together
  
  print("The solution is: ", + answer) # This outputs the divided numbers
