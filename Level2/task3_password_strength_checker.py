"""
Level 2 - Task 3: Password Strength Checker
Evaluates password strength based on length, uppercase/lowercase letters,
digits, and special characters.
"""

import re

def check_password_strength(password):
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g. !@#$%).")

    # Map score out of 5 to a strength label
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    strength, feedback = check_password_strength(user_password)

    print(f"\nPassword strength: {strength}")
    if feedback:
        print("Suggestions to improve:")
        for tip in feedback:
            print(f"  - {tip}")
    else:
        print("Great password!")
