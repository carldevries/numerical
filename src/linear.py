import copy

# minors determines the minors for each element in the given matrix or a given
# row in the matrix.  The default process is to return a complete matrix of
# minors. If a row is given as an optional argument, then only a single row
# with the minors for the elements in that row are calculated.
# Inputs:
#   matrix - A matrix with single, numerical values given for each element. The
#      acceptable matrix format is a two dimensional list for which the first
#      element specifies the row and the second index specifies the column.
#   expanded_row_index - An index 1 <= x <= len(matrix) which identifies a
#      specific row to calculate minors. An index less than 1 generates the
#      default complete matrix of minors. An index greater than the length of
#      the matrix returns an empty matrix(list).
# Outputs:
#   
def minors(matrix, expanded_row_index=-1):

    if is_square(matrix):

        # Lower and upper limits for iteration set to cover the entire matrix.
        matrix_row_start = 0
        matrix_row_end = len(matrix)
        matrix_column_start = 0
        matrix_column_end = len(matrix[0])

        # If a row is given as an argument and within the bounds 1 to n then
        if expanded_row_index > 0:
            
            if expanded_row_index > len(matrix):
                return []
                
            matrix_row_start = expanded_row_index - 1
            matrix_row_end = expanded_row_index
        
        # Add functionality to handle column expansion

        minors = []
        # Iterate over each row for the purpose of selecting an element to determine the minor of.
        for element_row_index in range(matrix_row_start, matrix_row_end):
            minors.append([])
            # Iterate over each column (element) for the purpose of selecting an element to determine the minor of.
            for element_column_index in range(matrix_column_start, matrix_column_end):
                minor = []
                # Iterate over each row for the purpose of adding elements to the current minor being created.
                for row_index in range(0, len(matrix)):
                    if element_row_index != row_index:
                        minor_row = []
                        # Iterate over each column(element) for the purpose of adding elements to the current minor being created.
                        for column_index in range(0, len(matrix[row_index])):
                            if element_column_index != column_index:
                                minor_row.append(matrix[row_index][column_index])

                        minor.append(minor_row)

                minors[len(minors) - 1].append(minor)
                
        return minors

    return []

def determinant(matrix):

    if is_square(matrix):

        # Base case: The determinant of a 1x1 matrix is the value in the matrix.
        if 1 == len(matrix):
            return matrix[0][0]
        # Base case: The determinant of a 2x2 matrix is computed as follows.
        elif 2 == len(matrix):
            return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
        # Recursive case: The determinant of a 3x3 or greater matrix is broken down
        # into smaller determinant evaluations.
        else:

            # Calculate only the minors for the selected row. Zero is the
            # default. Optimizations for the row with the most zeros to come.
            selected_minors = minors(matrix, expanded_row_index=0)
            minor_row = selected_minors[0]

            # Calculate the determinant for each minor in the row, .
            determinants = []
            for minor_index in range(0, len(minor_row)):
                minor_determinant = determinant(minor_row[minor_index])
                determinants.append(minor_determinant)

            #Determine the cofactors for the matrix.
            selected_cofactors = cofactors(matrix)
            expanded_cofactors_row = selected_cofactors[0]

            # Sum the products of the elements in the expanded row and their cofactors.
            final_determinant = 0;
            for index in range(0, len(selected_cofactors)):
                final_determinant += expanded_cofactors_row[index] * determinants[index]

            return final_determinant

    return []

# cofactors determines the cofactors of a matrix by adding the row index and
# the column index and if the sum is odd then multiplying the element by -1.
# Inputs:
#   matrix - A matrix with single, numerical values given for each element. The
#      acceptable matrix format is a two dimensional list for which the first
#      element specifies the row and the second index specifies the column.
# Outputs:
#   cofactors - A matrix containing the cofactors for the matrix given as the
#     function argument.

def cofactors(matrix):

    cofactors = copy.deepcopy(matrix)
    for row in range(0, len(cofactors)):
        for column in range(0, len(cofactors[row])):
            if (row + column) % 2 != 0:
                cofactors [row][column] =  -1 * cofactors[row][column]

    return cofactors

# is_square determines if the given matrix is square.
# Inputs:
#   matrix - A matrix created  using the acceptable matrix format of a two
#      dimensional list for which the first element specifies the row and the
#      second index specifies the column.
# Outputs:
#   A boolean value (True/False) representing whether the matrix is square.

def is_square(matrix):

    if (len(matrix) == 0):
        return False
        
    nrows = len(matrix)
    for rows in matrix:
        if nrows != len(rows):
            return False

    return True

# is_upper_triangular_matrix determines whether the matrix given meets the
# criteria for an upper triangular matrix. To meet the criteria, the matrix
# must only contain non-zero values along it's diagonal or above.
# Inputs:
#   matrix - A matrix with single, numerical values given for each element. The
#      acceptable matrix format is a two dimensional list for which the first
#      element specifies the row and the second index specifies the column.
# Outputs:
#   A boolean value (True/False) representing whether the matrix is and upper
#      triangular matrix.
def is_upper_triangular_matrix(matrix):

    if is_square(matrix):
    
        for i in range(1, len(matrix)):
            for j in range(0, i):
                if matrix[i][j] != 0:
                    return False

        return True

    return False;