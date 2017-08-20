import pytest
from math import pow
from ..root import regula_falsi
from test_helper  import almost_equal

def test_regula_falsi_quadratic():
    f = lambda x : pow(x, 2) - 1
    xl = 0
    xu = 5
    e = 0.0001

    xr, i = regula_falsi(xl, xu, f, e)
    assert almost_equal(1, xr, 0.0001)
    assert 27 == i

def test_regula_falsi_quadratic_no_root():
    f = lambda x : pow(x, 2) + 1
    xl = 0
    xu = 5
    e = 0.0001

    with pytest.raises(ValueError, message = 'Check the function contains at least one root and the upper and lower bounds surround the root.'):
        xr, i = regula_falsi(xl, xu, f, e)

def test_regula_falsi_quadratic_no_root_defined_max_iter():
    f = lambda x : pow(x, 2) + 1
    xl = 0
    xu = 5
    e = 0.0001
    n = 65

    with pytest.raises(ValueError, message = 'Check the function contains at least one root and the upper and lower bounds surround the root.'):
        xr, i = regula_falsi(xl, xu, f, e, n)

def test_regula_falsi_linear():
    f = lambda x : (5 * x) - 25
    xl = 0
    xu = 18
    e = 0.0001
    n = 10

    xr, i = regula_falsi(xl, xu, f, e, n)
    assert 1 == i

def test_reg_false():
    f = lambda x : pow(x, 2)
    xl = 5
    xu = 5
    e = 0.0001

    with pytest.raises(ValueError, message = 'Check the function contains at least one root and the upper and lower bounds surround the root.'):
        xr, i = regula_falsi(xl, xu, f, e)
