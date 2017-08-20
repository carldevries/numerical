import pytest
from ..ode import rk4
from test_helper import almost_equal
import math

resources_path = 'src\\test\\resources\\'

@pytest.mark.usefixture('rk4_results_one')
def test_one(rk4_results_one):

    functionOne = lambda x, y : x * math.sqrt(y[0])
    functions = [functionOne]
    inits = [4]
    data = rk4(inits, 1, 1.5, 5, functions)

    assert almost_equal(rk4_results_one[0][0], data[0][0], .0001)
    assert almost_equal(rk4_results_one[0][1][0], data[0][1][0], .0001)
    assert almost_equal(rk4_results_one[1][0], data[1][0], .0001)
    assert almost_equal(rk4_results_one[1][1][0], data[1][1][0], .0001)
    assert almost_equal(rk4_results_one[2][0], data[2][0], .0001)
    assert almost_equal(rk4_results_one[2][1][0], data[2][1][0], .0001)
    assert almost_equal(rk4_results_one[3][0], data[3][0], .0001)
    assert almost_equal(rk4_results_one[3][1][0], data[3][1][0], .0001)
    assert almost_equal(rk4_results_one[4][0], data[4][0], .0001)
    assert almost_equal(rk4_results_one[4][1][0], data[4][1][0], .0001)

@pytest.fixture(scope='module')
def rk4_results_one():

    rk4_results_one = open(resources_path + 'rk4_results_one.dat')
    return load_rk4_results(rk4_results_one)

###################################HELPERS#####################################
def load_rk4_results(results):

    results = results.readlines()
    expected_data = []
    
    for line in results:

        expected_data.append([])
        values = line.split(',')
        expected_data[len(expected_data) - 1].append(float(values[0]))
        expected_data[len(expected_data) - 1].append([float(values[1])])

    return expected_data