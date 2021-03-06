'''
# The code below does not seem to work as intended
import sys
modulename = 'numpy'
if modulename not in sys.modules:
    print('You have not imported the {} module'.format(modulename))
'''
import numpy
import pandas


def my_triangular_number(n):
    return (n*(n+1))/2


def my_inv_triangular_number(n):
    return int(-0.5+numpy.sqrt(2*n+1/4))


def my_fun(X, Y):
    return 2*X**2-0.5*Y**3+0.01*X**6*Y-X**4*Y**2

#fixme: This can probably be solved much prettier by returning a function taking c as an argument
# instead of returning a numerical value.
# The solution is ugly(?) but it seems to work.
def general_polynomial(c, X, Y):
    result = numpy.zeros(X.shape)
    n = c.__len__()
    d = my_inv_triangular_number(n)
    k = 0
    for i in range(d):
        if i == 0:
            result += c[k]
            k += 1
        else:
            for j in range(i+1):
                result += c[k]*X**j*Y**(i-j)
                k += 1
    return result


def sample_data(X, Y, Z, n):
    '''
    :param X:
    Meshgrid in x
    :param Y:
    Meshgrid in y
    :param Z:
    Scalar field generated by a function in two variables
    :param n:
    Number of data points in the returned data set
    :return:
    A pandas dataframe from the generated data that will be fitted against
    '''
    shape = Z.shape
    rand_index_x = [numpy.random.randint(0, shape[0]) for x in range(n)]
    rand_index_y = [numpy.random.randint(0, shape[1]) for y in range(n)]

    x = X[rand_index_x, rand_index_y]
    y = Y[rand_index_x, rand_index_y]
    z = Z[rand_index_x, rand_index_y]

    data = numpy.array([x, y, z]).transpose()
    df = pandas.DataFrame(data, columns=['x', 'y', 'z'])

    return df
