"""
Level 1 - Task 3: Email Validator
Validates whether a given string is a valid email address using regex.
Checks for: text before @, an @ symbol, a domain name, and a valid extension.
"""

import re

def is_valid_email(email):
    # Pattern breakdown:
    # ^[a-zA-Z0-9._%+-]+   -> one or more allowed characters before the @
    # @                    -> literal @ symbol
    # [a-zA-Z0-9.-]+       -> domain name (letters, numbers, dots, hyphens)
    # \.[a-zA-Z]{2,}$      -> a dot followed by 2+ letters (e.g. .com, .org)
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


if __name__ == "__main__":
    test_emails = [
        "test@example.com",
        "invalid.email.com",
        "user@domain",
        "name.surname@company.co.in",
        "@missingusername.com",
        "no_at_symbol.com"
    ]

    print("Running built-in test cases:")
    for email in test_emails:
        print(f"{email:30} -> {'Valid' if is_valid_email(email) else 'Invalid'}")

    print()
    user_email = input("Enter an email to validate: ")
    print("Valid email!" if is_valid_email(user_email) else "Invalid email.")
