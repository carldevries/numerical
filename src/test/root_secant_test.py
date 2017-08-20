import pytest
from math import pow
from ..root import secant
from test_helper  import almost_equal

def test_secant_quadratic():

    f = lambda x : pow(x, 2) - 1
    x1 = 5
    x2 = 6
    e = 0.0001
    n = 100

    xr, i = secant(x1, x2, f, e, n)
    assert almost_equal(1, xr, 0.0001)
    assert 7 == i

def test_secant_quadratic_no_root():
    f = lambda x : pow(x, 2) + 1
    x1 = 5
    x2 = 6
    e = 0.0001
    n = 100

    xr, i = secant(x1, x2, f, e, n)
    assert 100 == i