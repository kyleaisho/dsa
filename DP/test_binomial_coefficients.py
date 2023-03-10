from .binomial_coefficient import binomial_coefficient


def test_binomial_coeffient():
    assert binomial_coefficient(1, 1) == 1
    assert binomial_coefficient(5, 5) == 1
    assert binomial_coefficient(5, 2) == 10
    assert binomial_coefficient(37, 4) == 66045
