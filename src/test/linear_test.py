###################################IMPORTS#####################################
import pytest
from ..linear import is_square, minors, cofactors, determinant, is_upper_triangular_matrix

###################################CONSTANTS###################################
resources_path = 'src\\test\\resources\\'

###################################TESTS#######################################
@pytest.mark.parametrize('matrix',
    [([[1, 2, 3],
       [2, 3, 4],
       [3, 4, 5]]),
       
    ([[1, 2, 3, 4],
      [2, 3, 4, 5],
      [3, 4, 5, 6],
      [4, 5, 6, 7]])
    ])
def test_is_square_true(matrix):

    assert True == is_square(matrix)

@pytest.mark.parametrize('matrix',
    [([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]),
    ([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]),
    ([[1, 2, 3], [2, 3, 4, 5], [3, 4, 5], [4, 5, 6]])
    ])
def test_is_square_false(matrix):

    assert False == is_square(matrix)

def test_cofactors_3x3():

    matrix = [[1, 1, 1],
              [1, 1, 1],
              [1, 1, 1]]
    
    expected_cofactors = [[1, -1, 1],
                          [-1, 1, -1],
                          [1, -1, 1]]

    actual_cofactors = cofactors(matrix)
    
    assert expected_cofactors == actual_cofactors
    assert expected_cofactors != matrix

def test_cofactors_4x4():

    matrix = [[1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 1]]
    
    expected_cofactors = [[1, -1, 1, -1],
                          [-1, 1, -1, 1],
                          [1, -1, 1, -1]]

    actual_cofactors = cofactors(matrix)
    
    assert expected_cofactors == actual_cofactors
    assert expected_cofactors != matrix

@pytest.mark.parametrize('matrix',
    [([[1, 2, 3],
       [0, 3, 4],
       [0, 0, 5]]),
       
    ([[1, 2, 3, 4],
      [0, 3, 4, 5],
      [0, 0, 5, 6],
      [0, 0, 0, 7]])
    ])
def test_is_upper_triangular_true(matrix):

    assert True == is_upper_triangular_matrix(matrix)

@pytest.mark.parametrize('matrix',
    [([[1, 2, 3],
       [2, 3, 4],
       [3, 4, 5]]),
       
    ([[1, 2, 3, 4],
      [2, 3, 4, 5],
      [3, 4, 5, 6],
      [4, 5, 6, 7]])
    ])
def test_is_upper_triangular_false(matrix):

    assert False == is_upper_triangular_matrix(matrix)

# Test row selections out of bounds
@pytest.mark.parametrize('given_expanded_row',
    [(1), (2), (3)])
def test_minor_row_inbounds_selection_3x3(given_expanded_row, expected_minor_3x3):

    matrix = [[1, 2, 3],
              [2, 3, 4],
              [3, 4, 5]]

    expected_minors = [expected_minor_3x3[given_expanded_row - 1]]
    actual_minors = minors(matrix, expanded_row_index=given_expanded_row)
    assert expected_minors == actual_minors

@pytest.mark.usefixture('expected_minor_4x4')
def test_matrix_of_minors_3x3(expected_minor_3x3):

    matrix = [[1, 2, 3],
              [2, 3, 4],
              [3, 4, 5]]

    actual_minors = minors(matrix)
    assert expected_minor_3x3 == actual_minors

@pytest.mark.parametrize('given_expanded_row',
    [(1), (2), (3), (4)])
def test_minor_row_selection_4x4(given_expanded_row, expected_minor_4x4):

    matrix = [[1, 2, 3, 4],
              [2, 3, 4, 5],
              [3, 4, 5, 6],
              [4, 5, 6, 7]]

    expected_minors = [expected_minor_4x4[given_expanded_row - 1]]
    actual_minors = minors(matrix, expanded_row_index=given_expanded_row)
    assert expected_minors == actual_minors

@pytest.mark.usefixture('expected_minor_4x4')
def test_matrix_of_minors_4x4(expected_minor_4x4):

    matrix = [[1, 2, 3, 4],
              [2, 3, 4, 5],
              [3, 4, 5, 6],
              [4, 5, 6, 7]]
              
    actual_minors = minors(matrix)
    assert expected_minor_4x4 == actual_minors
    
@pytest.mark.parametrize('given_expanded_row',
    [(1), (2), (3)])
def test_minor_row_selection_3x3_2(given_expanded_row, expected_minor_3x3_2):

    matrix = [[2, -1, -2],
              [-5, 3, 4],
              [-2, 1, -1]]

    expected_minors = [expected_minor_3x3_2[given_expanded_row - 1]]
    actual_minors = minors(matrix, expanded_row_index=given_expanded_row)
    assert expected_minors == actual_minors
    
@pytest.mark.usefixture('expected_minor_3x3_2')
def test_matrix_of_minors_3x3_2(expected_minor_3x3_2):

    matrix = [[2, -1, -2],
              [-5, 3, 4],
              [-2, 1, -1]]

    actual_minors = minors(matrix)
    assert expected_minor_3x3_2 == actual_minors

@pytest.mark.parametrize('given_expanded_row',
    [(4), (5), (100)])
def test_minor_row_abovebounds_selection_3x3(given_expanded_row, expected_minor_3x3):

    matrix = [[1, 2, 3],
              [2, 3, 4],
              [3, 4, 5]]

    actual_minors = minors(matrix, expanded_row_index=given_expanded_row)
    assert [] == actual_minors

@pytest.mark.parametrize('given_expanded_row',
    [(0), (-1), (-3)])
def test_minor_row_belowbounds_selection_3x3(given_expanded_row, expected_minor_3x3):

    matrix = [[1, 2, 3],
              [2, 3, 4],
              [3, 4, 5]]

    actual_minors = minors(matrix)
    assert expected_minor_3x3 == actual_minors

def test_minor_matrix_not_square_3x3():

    matrix = [[1, 2, 3, 4],
              [2, 3, 4, 5],
              [3, 4, 5, 6]]

    actual_minors = minors(matrix)
    assert [] == actual_minors

def test_determinant_3x3_2():

    matrix = [[2, -1, -2],
              [-5, 3, 4],
              [-2, 1, -1]]

    actual_determinant = determinant(matrix)
    assert -3 == actual_determinant

def test_determinant_2x2():

    matrix = [[2, -1],
              [-5, 3]]

    actual_determinant = determinant(matrix)
    assert 1 == actual_determinant

###################################FIXTURES####################################

@pytest.fixture(scope='module')
def expected_minor_4x4():

    minor_4x4 = open(resources_path + 'minor_4x4.dat')
    return load_expected_matrix_of_minors(minor_4x4)
    
@pytest.fixture(scope='module')
def expected_minor_3x3():

    minor_3x3 = open(resources_path + 'minor_3x3.dat')
    return load_expected_matrix_of_minors(minor_3x3)
    
@pytest.fixture(scope='module')
def expected_minor_3x3_2():

    minor_3x3_2 = open(resources_path + 'minor_3x3_2.dat')
    return load_expected_matrix_of_minors(minor_3x3_2)

###################################HELPERS#####################################
def load_expected_matrix_of_minors(minor_file):

    minor_raw = minor_file.readlines()

    expected_minors = []
    expected_minors_row = []
    expected_minor = []

    for line in minor_raw:
        if line.find('---') == 0:
            expected_minors_row.append(expected_minor)
            expected_minor = []
        elif line.find('...') == 0:
            expected_minors.append(expected_minors_row)
            expected_minors_row = []
        else:
            values = line.split(',')
            minor_row = []
            for value in values:
                minor_row.append(int(value))
            expected_minor.append(minor_row)
    return expected_minors