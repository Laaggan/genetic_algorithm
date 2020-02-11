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
        assert N % 2 == 0, 'N must be a even number'

        self.N = N
        self.n = n
        self.k = k
        self.value_range = value_range

        self.population = np.zeros([N, k*n])
        self.InitializePopulation()
        self.decodedPopulation = np.zeros([N, n])
        self.DecodeChromosome()
        self.fitness = np.zeros([N, 1])
        self.current_generation = 0

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

    def roulette_wheel_selection(self):
        # Does it matter if it is with our without replacement?
        standardized_fitness = self.fitness/sum(self.fitness)
        cum_sum_fitness = np.cumsum(standardized_fitness)
        # Assigned to -1 since that is not a valid index
        breeders = [-1, -1]

        # Choose 2 chromosome that will form the next generation
        for j in range(2):
            selector = np.random.rand()
            for i, f in enumerate(cum_sum_fitness):
                if f > selector:
                    breeders[j] = i
                    break
                elif i == self.N-1:
                    breeders[j] = self.N-1
                    break
        return breeders

    def crossover(self, c1, c2):
        crossover_point = np.random.randint(0, len(c1))
        c1_prime = np.zeros(c1.shape)
        c2_prime = np.zeros(c2.shape)

        c1_prime[0:crossover_point] = c1[0:crossover_point]
        c1_prime[crossover_point:] = c2[crossover_point:]

        c2_prime[0:crossover_point] = c2[0:crossover_point]
        c2_prime[crossover_point:] = c1[crossover_point:]

        return c1_prime, c2_prime

    def mutation(self, c1, c2):
        p_mut = 0.02
        for i in range(len(c1)):
            p1 = np.random.rand()
            p2 = np.random.rand()
            #fixme: code below returns signed zeros which is kinda ugly
            if p1 < p_mut:
                c1[i] = -1*(c1[i] - 1)
            if p2 < p_mut:
                c2[i] = -1*(c2[i] - 1)
        return c1, c2


    def create_next_generation(self, new_fitness):
        next_generation = np.zeros(self.population.shape)
        self.fitness = new_fitness
        selection = self.roulette_wheel_selection()
        c1 = self.population[selection[0], :]
        c2 = self.population[selection[1], :]

        for i in range(self.N//2):
            c1_p, c2_p = self.crossover(c1, c2)
            c1_p, c2_p = self.mutation(c1_p, c2_p)
            next_generation[2 * i, :] = c1_p
            next_generation[2 * i + 1, :] = c2_p



'''
test = GeneticAlgorithm(10, 10, 10)
test.InitializePopulation()
test.DecodeChromosome()
print(test.decodedPopulation)
'''