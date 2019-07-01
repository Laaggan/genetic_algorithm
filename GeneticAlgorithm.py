import numpy as np
from MyLib import FitnessFunction

class GeneticAlgorithm:
    def __init__(self, N, n, k):
        '''
        :param N:
        Number of individuals in the population
        :param n:
        is the number of variables of the target function
        :param k:
        k is the number of bits representing our function
        '''
        self.population = np.zeros([N, k*n])
        self.decodedPopulation = np.zeros([N, n])
        self.fitness = np.zeros([N, 1])

    def RetrieveScalarFields(self, Zapprox, Z):
        '''
        Help function to more easily evaluate fitness
        :param Zapprox:
        The values approximated by the chromosome
        :param Z:
        The target values
        :return:
        '''
        self.Zapprox = Zapprox
        self.Z = Z

    def InitializePopulation(self):
        for i in range(self.population.shape[0]):
            for j in range(self.population.shape[1]):
                if np.random.rand() < 0.5:
                    self.population[i, j] = 1

    #fixme: You don't know the range of possible values for the coefficients of the polynomial. How do you solve this?
    def DecodeChromosome(self):
        for i, chromosome in enumerate(self.population):
            for j, g in enumerate(chromosome):
                self.decodedPopulation[i] += 2**-j*g
        #For the time being I will assume coefficients between [-10, 10]
        self.decodedPopulation = -10 + 2*10*self.decodedPopulation

    def EvaluateFitness(self):
        # I will use the mean squared error as the error function?
        for i, Zi in enumerate(self.Zapprox):
            self.fitness[i] = np.sum(Zi - self.Z)


test = GeneticAlgorithm(10, 10, 10)
test.InitializePopulation()
test.DecodeChromosome()

print(test.decodedPopulation)