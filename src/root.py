from math import fabs

# newton_raphson is an open root-finding method which utilizes both the 
# function and its analytical derivate to approximate the root.
# Inputs:
#   initial_root - An initial guess for the location of the function's root.
#   function - A lambda function to evaluate the single variable function.
#   derivative - A lambda function to evaluate the single variable derivative.
#   error - An error tolerance which specifies the function can return an
#      approximation to the root given the absolute value of the function
#      evaluates to a value less than the tolerance.
#   max_iterations - The maximum number of allowed iterations before the
# function returns without finding a root.
# Outputs:
#   x - An approximation to the root within the specified error tolerance. If
#      the maximum number of iterations is reached, then None is returned.
#   i - The number of iteration required to reach an approximation within the
#      given error tolerance.

def newton_raphson(initial_root, function, derivative, error, max_iterations):

    root = initial_root
    iterations = 0
    while fabs(function(root)) > error and iterations < max_iterations:

        root = root - (function(root) / derivative(root))
        iterations = iterations + 1

    if iterations == max_iterations:
        return None, iterations

    return root, iterations

# bisection is a closed root-finding method which guarantees convergence to a
# root (not necessarily in a given number of iterations) given the upper bound
# and lower bound properly surround the root. Bisection approximates the root
# for each iteration as the midpoint between the upper bound and lower bound
# for each iteration.
# Inputs:
#   lower_bound - The lower bound of a range which the root should be within.
#   upper_bound - The upper bound of a range which the root should be within.
#   function - A lambda function to evaluate the single variable function.
#   error - An error tolerance which specifies the function can return an
#      approximation to the root given the absolute value of the function
#      evaluates to a value less than the tolerance.
#   max_iterations - The maximum number of allowed iterations before the
# function returns without finding a root.
# Outputs:
#   x - An approximation to the root within the specified error tolerance. If
#      the maximum number of iterations is reached, then None is returned.
#   i - The number of iteration required to reach an approximation within the
#      given error tolerance.

def bisection(lower_bound, upper_bound, function, error, max_iterations=10000):
    
    _validate_initial_bounds(function, lower_bound, upper_bound)

    root = (lower_bound + upper_bound) / 2
    iterations = 0
    while fabs(function(root)) > error and iterations < max_iterations:

        root = (lower_bound + upper_bound) / 2

        if (function(lower_bound) * function(root)) > 0:
            lower_bound = root
        else:
            upper_bound = root

        iterations = iterations + 1

    if iterations == max_iterations:
        return None, iterations

    return root, iterations

# regula falsi (false position) is a closed root-finding method which
# guarantees convergence to a root (not necessarily in a given number of
# iterations) given the upper bound and lower bound properly surround the root.
# Regula Falsi utilizes the linear slope between the upper bound and lower
# bound to approximate the root assuming it trends similarly to the actual
# function.
# Inputs:
#   lower_bound - The lower bound of a range which the root should be within.
#   upper_bound - The upper bound of a range which the root should be within.
#   function - A lambda function to evaluate the single variable function.
#   error - An error tolerance which specifies the function can return an
#      approximation to the root given the absolute value of the function
#      evaluates to a value less than the tolerance.
#   max_iterations - The maximum number of allowed iterations before the
# function returns without finding a root.
# Outputs:
#   x - An approximation to the root within the specified error tolerance. If
#      the maximum number of iterations is reached, then None is returned.
#   i - The number of iteration required to reach an approximation within the
#      given error tolerance.

def regula_falsi(lower_bound, upper_bound, function, error, max_iterations = 10000):

    _validate_initial_bounds(function, lower_bound, upper_bound)

    root = lower_bound
    iterations = 0
    while fabs(function(root)) > error and iterations < max_iterations:

        denominator = (function(lower_bound) - function(upper_bound))
        if denominator == 0:
            raise ZeroDivisionError('f(lower_bound) - f(upper_bound) equals zero. Args: ' + str(lower_bound) + ', ' + str(upper_bound) + ', ' + getsource(function) + ', ' + str(error) + ', ' + str(max_iter) + ', iter =' + str(iterations))

        root = ((function(lower_bound) * upper_bound) - (function(upper_bound) * lower_bound)) / denominator

        if (function(lower_bound) * function(root)) > 0:
            lower_bound = root
        else:
            upper_bound = root

        iterations = iterations + 1

    if iterations == max_iterations:
        return None, iterations

    return root, iterations

# secant is an open root-finding method which utilizes two  initial
# approximations which are not required to surround the actual root. The method
# utilizes the linear slope between the two approximations to generate a new
# approximation assuming for small distances, the linear slope approximates the
# slope of the actual function.
# Inputs:
#   x1 - An initial approximation for the actual root.
#   x2 - A second initial approximation for the actual root.
#   function - A lambda function to evaluate the single variable function.
#   error - An error tolerance which specifies the function can return an
#      approximation to the root given the absolute value of the function
#      evaluates to a value less than the tolerance.
#   max_iterations - The maximum number of allowed iterations before the
# function returns without finding a root.
# Outputs:
#   x - An approximation to the root within the specified error tolerance. If
#      the maximum number of iterations is reached, then None is returned.
#   i - The number of iteration required to reach an approximation within the
#      given error tolerance.
def secant(x1, x2, function, error, max_iterations):

    root = x1
    iterations = 0
    while fabs(function(root)) > error and iterations < max_iterations:

        root = x1 - ((function(x1) * (x2 - x1)) / (function(x2) - function(x1)))

        x2 = x1
        x1 = root

        iterations = iterations + 1

    if iterations == max_iterations:
        return None, iterations

    return root, iterations

def _validate_initial_bounds(function, lower_bound, upper_bound):

    if (function(lower_bound) * function(upper_bound)) > 0:
       raise ValueError('Check the function contains at least one root and the upper and lower bounds surround the root.')