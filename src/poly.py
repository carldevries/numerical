

# horners_scheme is a method for evaluating an nth degree polynomial.
# Inputs:
#   x - The independent variable used to evaluate the polynomial.
#   coefficients - An array of the polynomial's coefficients.
#      Array index:0 1 2 3 4 5 6 7 8 9
#      Degree     :9 8 7 6 5 4 3 2 1 0
#Outputs:
#   y - The value of the polynomial evaluated at the value x.

def horners_scheme(x, coefficients):

    y = 0
    for coefficient in coefficients:

        y = (y * x) + coefficient

    return y