import numpy as np
from MyLib import *

class GeneticAlgorithm:
    def __init__(self, N, n, k, value_range=(-10, 10)):
        '''
        :param N:
        Number of individuals in the population
        :param n:
        is the number of variables of the target function
        :param k:
        k is the number of bits representing our function
        '''
        assert value_range[0] < value_range[1], 'Must be a valid range'

        self.N = N
        self.n = n
        self.k = k
        self.value_range = value_range

        self.population = np.zeros([N, k*n])
        self.InitializePopulation()
        self.decodedPopulation = np.zeros([N, n])
        self.DecodeChromosome()
        self.fitness = np.zeros([N, 1])

    #fixme: Why is this not in __init__()?
    def RetrieveScalarFields(self, Z_hat, Z):
        '''
        Help function to more easily evaluate fitness
        :param Z_hat:
        The values approximated by the chromosome
        :return:
        '''
        self.Z_hat = Z_hat

    def InitializePopulation(self):
        '''
        Randomly initializes the population with a binary encoding scheme with equal probability of a one or a zero
        :return:
        '''
        for i in range(self.population.shape[0]):
            for j in range(self.population.shape[1]):
                if np.random.rand() < 0.5:
                    self.population[i, j] = 1

    def DecodeChromosome(self):
        for i in range(self.N):
            chromosome = self.population[i, :]
            for j in range(self.n):
                decoded_value = 0
                variable = chromosome[j*self.k:((j+1)*self.k-1)]
                for l, x in enumerate(variable):
                    decoded_value += 2**(-(l+1))*x
                transformed_value = self.value_range[0] + 2*self.value_range[1]*decoded_value
                self.decodedPopulation[i, j] = transformed_value

    def EvaluateFitness(self, X, Y, Z_hat=None):
        # I will use the mean squared error as the error function?
        Z_hat = GeneralPolynomial(self.decodedPopulation[0, :], X, Y)
        try:
            for i, Zi in enumerate(self.Z_hat):
                self.fitness[i] = np.sum(np.power(Zi - self.Z, 2))
        except:
            self.fitness = np.sum(np.power(self.Z_hat - self.Z, 2))

    def GeneralPolynomial(c, X, Y):
        result = numpy.zeros(X.shape)
        n = c.__len__()
        d = MyInvTriangularNumber(n)
        k = 0
        for i in range(d):
            if i == 0:
                result += c[k]
                k += 1
            else:
                for j in range(i + 1):
                    result += c[k] * X ** j * Y ** (i - j)
                    k += 1
        return result

'''
test = GeneticAlgorithm(10, 10, 10)
test.InitializePopulation()
test.DecodeChromosome()
print(test.decodedPopulation)
'''