"""
Level 1 - Task 5: Palindrome Checker
Checks whether a given string is a palindrome (reads the same backward as forward).
Ignores spaces, punctuation, and letter case for a more robust check.
"""

def is_palindrome(text):
    # Keep only alphanumeric characters and make everything lowercase
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    # Compare the cleaned string to its reverse
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    test_words = ["madam", "racecar", "hello", "A man a plan a canal Panama"]

    print("Running built-in test cases:")
    for word in test_words:
        print(f"'{word}' -> {'Palindrome' if is_palindrome(word) else 'Not a palindrome'}")

    print()
    user_input = input("Enter a word or phrase to check: ")
    if is_palindrome(user_input):
        print("That's a palindrome!")
    else:
        print("That's not a palindrome.")
