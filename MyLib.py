'''
# The code below does not seem to work as intended
import sys
modulename = 'numpy'
if modulename not in sys.modules:
    print('You have not imported the {} module'.format(modulename))
'''
import numpy
import pandas

def MyFun(X, Y):
    return 2*X**2-0.5*Y**3

def SampleData(X, Y, Z, n):
    '''
    :param X:
    Meshgrid
    :param Y:
    Meshgrid
    :param Z:
    Scalar field from a surface
    :param n:
    Number of data points in the returned data set
    :return:
    A pandas dataframe from the generated data that will be fitted against
    '''
    shape = Z.shape
    #fixme: The x and y's can probably be removed somehow making the code cleaner
    randIndexX = [numpy.random.randint(0, shape[0]) for x in range(n)]
    randIndexY = [numpy.random.randint(0, shape[1]) for y in range(n)]

    x = X[randIndexX, randIndexY]
    y = Y[randIndexX, randIndexY]
    z = Z[randIndexX, randIndexY]

    data = numpy.array([x,y,z]).transpose()
    df = pandas.DataFrame(data, columns=['x', 'y', 'z'])

    return df