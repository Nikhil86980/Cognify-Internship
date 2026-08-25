"""
Level 2 - Task 4: Fibonacci Sequence
Generates the Fibonacci sequence up to a given number of terms.
"""

def generate_fibonacci(num_terms):
    if num_terms <= 0:
        return []
    elif num_terms == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < num_terms:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)

    return sequence


if __name__ == "__main__":
    n = int(input("Enter the number of terms for the Fibonacci sequence: "))
    result = generate_fibonacci(n)
    print(f"Fibonacci sequence with {n} terms:")
    print(result)
