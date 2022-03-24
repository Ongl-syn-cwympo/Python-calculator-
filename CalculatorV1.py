# Program; make a program simple calculator for all functions
# Program can only handle 2 inputs
# Python code 
# Created by Ongl syn cwympo 
# https://github.com/Ongl-syn-cwympo


print("What would you like to use the calculator for?")
print("1. Adding")
print("2. Subtracting")
print("3. Multiplication")
print("4. Division")

Num = input()

if Num == "1":
  print("+ Addition calculator +")
  x = input("Type a number: ") # Asks user for the input
  y = input("Type another number: ") # Asks user for the second input
  
  answer = int(x) + int(y) # This function adds both numbers inputed together
  
  print("The solution is: ", + answer) # This outputs the combined numbers


if Num == "2":
  print("- SUbtraction calculator -")
  x = input("Type a number: ") # Asks user for the input
  y = input("Type another number: ") # Asks user for the second input
  
  answer = int(x) - int(y) # This function subs both numbers inputed together
  
  print("The solution is: ", + answer) # This outputs the subtracted numbers


if Num == "3":
  print("* Multiplication calculator *")
  x = input("Type a number: ") # Asks user for the input
  y = input("Type another number: ") # Asks user for the second input
  
  answer = int(x) * int(y) # This function multiplies both numbers inputed together
  
  print("The solution is: ", + answer) # This outputs the multiplied numbers


if Num == "4":
  print("/ Division calculator /")
  x = input("Type a number: ") # Asks user for the input
  y = input("Type another number: ") # Asks user for the second input
  
  answer = int(x) / int(y) # This function divides both numbers inputed together
  
  print("The solution is: ", + answer) # This outputs the divided numbers
