# pylint: disable=missing-docstring
import pytest
from prime import generate_prime_factors
"""
The test module for Prime Factors
"""
def test_prime_factor_1():
    """
    Given a prime number 1
    """
    primes = []
    assert generate_prime_factors(1, primes) == primes

def test_prime_factor_2():
    """
    Given a prime number 2
    """
    primes = [2]
    assert generate_prime_factors(2, primes) == primes

def test_prime_factor_3():
    """
    Given a prime number 3
    """
    primes = [3]
    assert generate_prime_factors(3, primes) == primes

def test_prime_factor_4():
    """
    Given a prime number 4
    """
    primes = [2, 2]
    assert generate_prime_factors(4, primes) == primes

def test_prime_factor_6():
    """
    Given a prime number 4
    """
    primes = [2, 3]
    assert generate_prime_factors(6, primes) == primes
