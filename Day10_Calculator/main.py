from art import logo

#Functions for each operator
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

#Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
  print(logo)
  n1 = float(input("Enter first number: "))
  operation_symbol = input("Pick an operation: ")
  n2 = float(input("Enter second number: "))

  for operation in operations:
    print(operation)

  selected_operator = operations[operation_symbol]
  ans = selected_operator(n1, n2)

  print(f"{n1} {operation_symbol} {n2} = {ans}")

  decision = input(
      "Do you want to continue? \'y' or \'e' to exit or \'n' to start a new calculation: ")

  while decision.lower() == 'y':
    operation_symbol = input("Pick an operation: ")
    n2 = float(input("Enter second number: "))

    for operation in operations:
      print(operation)

    n1 = ans
    selected_operator = operations.get(operation_symbol)
    ans = selected_operator(n1, n2)

    print(f"{n1} {operation_symbol} {n2} = {ans}")
    decision = input(
      "Do you want to continue? \'y' or \'e' to exit or '\'n' to start a new calculation: ")

  if decision.lower() == 'n':
    calculator()
  if decision.lower() == 'e':
    exit()


calculator()
