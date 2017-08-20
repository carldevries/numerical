import pytest
from math import pow
from ..root import bisection
from test_helper  import almost_equal

ROOT_TOLERANCE = 0.00001

def test_bisection_quadratic():
    f = lambda x : pow(x, 2) - 1
    xl = 0
    xu = 5
    e = 0.0001

    xr, i = bisection(xl, xu, f, e)
    assert 1 == pytest.approx(xr)
    assert 2 == i

def test_bisection_quadratic_no_root_default_max_iter_raise_ValueError():
    f = lambda x : pow(x, 2) + 1
    xl = 0
    xu = 5
    e = 0.0001

    with pytest.raises(ValueError, message = 'Check the function contains at least one root and the upper and lower bounds surround the root.'):
        xr, i = bisection(xl, xu, f, e)

def test_bisection_quadratic_invalid_bounds_raise_ValueError():
    f = lambda x : pow(x, 2) - 1
    xl = 5
    xu = 11
    e = 0.0001

    with pytest.raises(ValueError, message = "Check the function contains at least one root and the upper and lower bounds surround the root."):
        xr, i = bisection(xl, xu, f, e)

def test_bisection_quadratic_no_root_raise_ValueError():
    f = lambda x : pow(x, 2) + 1
    xl = 0
    xu = 5
    e = 0.0001
    n = 75

    with pytest.raises(ValueError, message = 'Check the function contains at least one root and the upper and lower bounds surround the root.'):
        xr, i = bisection(xl, xu, f, e, n)

def test_bisection_linear():
    f = lambda x : (5 * x)  - 25
    xl = 0
    xu = 18
    e = 0.0001
    n = 75

    xr, i = bisection(xl, xu, f, e, n)
    assert almost_equal(5, xr, ROOT_TOLERANCE)
    assert 4 == i