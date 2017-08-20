import pytest
from .. import poly

def test_coef_2_5_10_x_3_equals_43():

    x = 3
    c = [2, 5, 10]
    assert 43 == poly.horners_scheme(x, c)

def test_coef_5_10_x_3_equals_25():

    x = 3
    c = [5, 10]
    assert 25 == poly.horners_scheme(x, c)

def test_coef_5_4_3_2_x_2_equals_64():

    x = 2
    c = [5, 4, 3, 2]
    assert 64 == poly.horners_scheme(x, c)
