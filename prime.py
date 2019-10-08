import sys
"""
prime.py -- Write the application code here
"""
# thirdAssignment
def generate_prime_factors(n):

    if type(n) is not int:
        raise ValueError
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
