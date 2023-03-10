from .binomial_coefficient import binomial_coefficient
from .fibonacci import fib


def test_binomial_coeffient():
    assert binomial_coefficient(1, 1) == 1
    assert binomial_coefficient(5, 5) == 1
    assert binomial_coefficient(5, 2) == 10
    assert binomial_coefficient(37, 4) == 66045


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2

    assert fib(23) == 28657
