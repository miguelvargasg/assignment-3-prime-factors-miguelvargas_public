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
    return primes
