"""
Level 1 - Task 1: String Reversal
Takes a string as input and returns the reverse of that string.
"""

def reverse_string(text):
    # Python slicing trick: [::-1] means "take the whole string, step backwards"
    return text[::-1]


# --- Test / Demo ---
if __name__ == "__main__":
    user_input = input("Enter a string to reverse: ")
    result = reverse_string(user_input)
    print(f"Reversed string: {result}")

    # Extra example matching the task description
    print(reverse_string("hello"))  # should print: olleh
