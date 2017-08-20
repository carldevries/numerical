from .. import root
import math
import pytest
from test_helper import almost_equal

ROOT_TOLERANCE = 0.00001

def test_newton_raphson_quadratic():

    f = lambda x : math.pow(x,2) - 1
    dfdx = lambda x : 2 * x
    x0 = 5
    e = 0.0001
    n = 10

    xr, i = root.newton_raphson(x0, f, dfdx, e, n)
    assert almost_equal(1, xr, ROOT_TOLERANCE)
    assert 5 == i

def test_newton_raphson_quadratic_no_root():

    f = lambda x : math.pow(x,2) + 1
    dfdx = lambda x : 2 * x
    x0 = 5
    e = 0.0001
    n = 50

    xr, i = root.newton_raphson(x0, f, dfdx, e, n)
    assert i == 50

def test_newton_raphson_linear():

    f = lambda x : (5 * x) - 25
    dfdx = lambda x : 5
    x0 = 0
    e = 0.0001
    n = 50

    xr, i = root.newton_raphson(x0, f, dfdx, e, n)
    assert almost_equal(5, xr, ROOT_TOLERANCE)
    assert 1 == i