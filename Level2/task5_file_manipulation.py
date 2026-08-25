"""
Level 2 - Task 5: File Manipulation
Reads a text file and counts the occurrences of each word.
Displays results in alphabetical order with their counts.

A sample.txt file is included in this folder for testing.
"""

import string

def count_word_occurrences(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()

    # Remove punctuation and make everything lowercase so
    # "Python" and "python," are counted as the same word
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.lower().split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


if __name__ == "__main__":
    filepath = input("Enter the path to a text file (or press Enter to use sample.txt): ").strip()
    if not filepath:
        filepath = "sample.txt"

    counts = count_word_occurrences(filepath)

    print("\nWord counts (alphabetical order):")
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")
