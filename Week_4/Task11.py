import math

def add(a, b):
  return a + b 
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a, b):
  if b!= 0:
    return a / b
  else:
    return "Error: Division by zero"
def raise_to(a, b):
    return a ** b
def find_square_root(num):
    if num < 0:
        return "Error: cannot find square root of a negative number"
    return math.sqrt(num)
    
while True: 
  print("Select operation")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Raise to power")
  print("6. Square root")
  print("7. Exit")

  choice = input("Enter choice 1-7:")
  if choice == '7':
    print("End of operation")
    break
  try:
    if choice == '6':
      number = float(input("Enter number:"))
      print("Result:", find_square_root(number))
    else:
      num1 = float(input("Enter first number:"))
      num2 = float(input("Enter second number:"))
    
      if choice == '1':
        print("Result:", add(num1, num2))
        continue
      elif choice == '2':
        print("Result:", subtract(num1, num2))
        continue
      elif choice == '3':
        print("Result:", multiply(num1, num2))
        continue
      elif choice == '4':
        print("Result:", divide(num1, num2))
        continue
      elif choice == '5':
        print("Result:", raise_to(num1, num2))
        continue
        break
      else:
        print("Invalid option! Please select from 1-7.")
  except ValueError: 
    print("Error due to invalid input. Enter numbers only")