def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot div by zero."

def calculator():
    while True:
        print("Simple Calculator")
        print("S. Add")
        print("O. Sub")
        print("W. Mul")
        print("M. Div")
        print("I. Leave")

        option = input("Enter operation option (S/O/W/M/I): ")

        if option == 'I':
            print("Leaving calculator. tata!")
            break

        if option not in ('S', 'O', 'W', 'M'):
            print("Unwell option. Please enter a valid operation.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if option == 'S':
            result = add(num1, num2)
        elif option == 'O':
            result = sub(num1, num2)
        elif option == 'W':
            result = mul(num1, num2)
        elif option == 'M':
            result = div(num1, num2)

        print(f"Result: {result}")

# Run the calculator infinitely
calculator()

            
