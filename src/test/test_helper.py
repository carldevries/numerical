from math import fabs

def almost_equal(expected, actual, threshold):
	
	print('Actual = ' + str(actual))
	return fabs(actual - expected) < threshold
	