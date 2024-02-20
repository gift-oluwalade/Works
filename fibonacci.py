import random

def generate_random_number():
    number = ''.join(str(random.randint(0, 1)) for _ in range(4))
    return int(number, 2)

def convert_to_base_10(number):
    base_10_number = 0
    for digit in str(number):
        base_10_number = base_10_number * 2 + int(digit)
    return base_10_number

random_number = generate_random_number()
base_10_number = convert_to_base_10(random_number)
print(base_10_number)

""" Sequence to run fibonnacci code with the sum of 50
def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

def sum_fibonacci_sequence(sequence):
    return sum(sequence)

fibonacci_sequence = fibonacci_sequence(50)
sum = sum_fibonacci_sequence(fibonacci_sequence)
print(sum)
"""