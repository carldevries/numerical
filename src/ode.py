#Loops through the Fourth Order Runge Kutta algorithm for each the numer of given steps
def rk4(initial_conditions, lower_bound, upper_bound, numberOfSteps, functions):

    n_eqns = len(initial_conditions)

    #Calculate parameters and store initial conditions
    step_size = (upper_bound - lower_bound) / numberOfSteps
    x = lower_bound

    y = [0] * n_eqns
    for i in range(n_eqns):
        y[i] = initial_conditions[i]

    #Create a data store
    data = [[0 for i in range(2)] for j in range(numberOfSteps + 1)]
    data[0][0] = x
    data[0][1] = y[:]
    
    #Integrate
    for i in range(numberOfSteps):

        _solve(x, y, step_size, n_eqns, functions)
        x += step_size

        data[i + 1][0] = x
        data[i + 1][1] = y[:]

    return data
    
#Calculates the a new y value for the current step
def _solve(x, y, step_size, n_eqns, functions):

    #Create temporary variables for x and y
    yk = [0] * n_eqns

    #Calculate k1 values
    xk = x
    for i in range(n_eqns):
        yk[i] = y[i]
    k1 = _feval(xk, yk, n_eqns, functions)
    
    #Calculate k2 values
    xk = x + (step_size / 2)
    for i in range(n_eqns):
        yk[i] = y[i] + (k1[i] * (step_size / 2))
    k2 = _feval(xk, yk, n_eqns, functions)

    #Calculate k3 values
    for i in range(n_eqns):
        yk[i] = y[i] + (k2[i] * (step_size / 2))
    k3 = _feval(xk, yk, n_eqns, functions)

    #Calculate k4 values
    xk = x + step_size
    for i in range(n_eqns):
        yk[i] = y[i] + (k3[i] * step_size)
    k4 = _feval(xk, yk, n_eqns, functions)

    #Calculate y values
    for i in range(n_eqns):
        y[i] = y[i] + (((step_size / 6) * (k1[i] + (2 * (k2[i] + k3[i])) + k4[i])))

#Evaluate each differential equation at the values x and y
def _feval(x, y, n_eqns, functions):

    k = [0] * n_eqns
    
    for i in range(n_eqns):
        k[i] = functions[i](x, y)

    return k
