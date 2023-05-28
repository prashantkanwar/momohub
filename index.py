def greet(name):
    """Prints a greeting message."""
    print(f"Hello, {name}!")

def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def main():
    # Prompt the user for their name
    name = input("Enter your name: ")

    # Greet the user
    greet(name)

    # Perform addition
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = add_numbers(num1, num2)
    multiplynumber = multiply_numbers(a,b)
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()

    