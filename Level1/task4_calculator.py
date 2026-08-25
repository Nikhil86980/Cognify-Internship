"""
Level 1 - Task 4: Calculator Program
Prompts the user for two numbers and an operator, then displays the result.
Supports +, -, *, /, %
"""

def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    elif operator == "%":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 % num2
    else:
        return "Error: Invalid operator"


def main():
    print("Simple Calculator (+, -, *, /, %)")
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /, %): ").strip()
    num2 = float(input("Enter the second number: "))

    result = calculate(num1, operator, num2)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
