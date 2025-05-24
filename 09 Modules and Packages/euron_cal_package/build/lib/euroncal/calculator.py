def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Raise a to the power of b."""
    return a ** b

def square_root(a):
    """Calculate square root of a."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5

def main():
    """Simple command line interface."""
    print("Welcome to Euroncal Calculator!")
    print("Operations: add, subtract, multiply, divide, power, sqrt, quit")
    
    while True:
        operation = input("\nEnter operation: ").lower().strip()
        
        if operation == 'quit':
            print("Goodbye!")
            break
        
        try:
            if operation == 'sqrt':
                num = float(input("Enter number: "))
                result = square_root(num)
                print(f"√{num} = {result}")
            
            elif operation in ['add', 'subtract', 'multiply', 'divide', 'power']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if operation == 'add':
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif operation == 'subtract':
                    result = subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                elif operation == 'multiply':
                    result = multiply(num1, num2)
                    print(f"{num1} × {num2} = {result}")
                elif operation == 'divide':
                    result = divide(num1, num2)
                    print(f"{num1} ÷ {num2} = {result}")
                elif operation == 'power':
                    result = power(num1, num2)
                    print(f"{num1} ^ {num2} = {result}")
            else:
                print("Unknown operation. Try: add, subtract, multiply, divide, power, sqrt, quit")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()