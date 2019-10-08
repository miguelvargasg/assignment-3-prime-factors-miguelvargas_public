# pylint: disable=missing-docstring
import pytest
from prime import generate_prime_factors
"""
The test module for Prime Factors
"""
def test_prime_factor():
    """
    Given a prime number
    """
    primes = []
    assert generate_prime_factors(1, primes) == primes
