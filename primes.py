"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    list = []
    current_integer = 0
    while len(list) < number_of_primes:
        current_integer += 1
        if is_prime(current_integer):
            list.append(current_integer)
    return list

def is_prime(integer):
    if integer <= 1:
        return False
    for factor in range(2, int(integer ** 0.5) + 1):
        if integer % factor == 0:
            return False
    else:
        return True
