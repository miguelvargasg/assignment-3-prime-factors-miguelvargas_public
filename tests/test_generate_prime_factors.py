# pylint: disable=missing-docstring
import pytest
from prime import generate_prime_factors
"""
The test module for Prime Factors
"""
def test_prime_factor_1():
    primes = []
    assert generate_prime_factors(1) == primes

def test_prime_factor_2():
    primes = [2]
    assert generate_prime_factors(2) == primes

def test_prime_factor_3():
    primes = [3]
    assert generate_prime_factors(3) == primes

def test_prime_factor_4():
    primes = [2, 2]
    assert generate_prime_factors(4) == primes

def test_prime_factor_6():
    primes = [2, 3]
    assert generate_prime_factors(6) == primes

def test_prime_factor_8():
    primes = [2, 2, 2]
    assert generate_prime_factors(8) == primes

def test_prime_factor_9():
    primes = [3, 3]
    assert generate_prime_factors(9) == primes
