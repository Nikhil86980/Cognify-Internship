"""
Level 1 - Task 2: Temperature Conversion
Converts temperature between Celsius and Fahrenheit based on user input.
"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose an option (1 or 2): ").strip()
    value = float(input("Enter the temperature value: "))

    if choice == "1":
        converted = celsius_to_fahrenheit(value)
        print(f"{value}°C is equal to {converted:.2f}°F")
    elif choice == "2":
        converted = fahrenheit_to_celsius(value)
        print(f"{value}°F is equal to {converted:.2f}°C")
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
