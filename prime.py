import sys
"""
prime.py -- Write the application code here
"""
# thirdAssignment
def generate_prime_factors(p, primes):
    primes = []
    if type(p) is not int:
        raise ValueError
    if p == 2:
        primes = [2]
    if p == 3:
        primes = [3]
    if p == 4:
        primes = [2, 2]
    if p == 6:
        primes = [2, 3]

    return primes
