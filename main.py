import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import copy
from my_lib import *
from genetic_algorithm import *

# Setting up the plotting
xmin, xmax = -2, 2
ymin, ymax = -2, 2
x = np.linspace(xmin, xmax)
y = np.linspace(ymin, ymax)
X, Y = np.meshgrid(x, y)
Z = my_fun(X, Y)

# Generating the data which we will fit the new function against
# n is the size of the data set
n = 10
data_set = sample_data(X, Y, Z, n)

# d is the degree of the polynomial
d = 7

# if the polynomial has degree d, the corresponding polynomial will have
# $$ c_{len} = \Sigma_{i=1}^d i = (d*(d+1))/2 $$. Meaning that
# c_len is the number of terms in a bivariate polynomial of degree d
c_len = int(my_triangular_number(d))
N = 50
k = 15
current_fitness = np.zeros((N,))
gen_alg = GeneticAlgorithm(N=N, n=c_len, k=k)

# The first chromosome in the genetic algorithm
c = gen_alg.decoded_population[0, :]

def calculate_fitness():
    for c_i in range(N):
        gen_alg.decode_chromosome()
        chromosome = gen_alg.decoded_population[c_i, :]
        # Calculate the predicted surface
        Z_hat = general_polynomial(chromosome, X, Y)
        Z_error = Z - Z_hat
        MSE = np.mean(np.power(Z_error, 2))
        # 1/MSE is fitness since the convention is to maximize fitness
        current_fitness[c_i] = 1/MSE

def save_my_fig(c, X, Y, generation):
    # Evaluating the current solution c producing the current approximation Z_hat
    Z_hat = general_polynomial(c, X, Y)

    # Setting up the plot for the target surface and the approximation surface
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.set_title('Predicted surface \nand target surface')
    ax1.set_yticks([])
    ax1.set_xticks([])
    ax1 = f.add_subplot(1, 2, 1, projection='3d')
    ax1.set_zlim(np.min(Z)-100, np.max(Z)+100)
    ax1.set_yticks([])
    ax1.set_xticks([])
    ax1.set_zticks([])
    #Z_error = Z - Z_hat
    surf1 = ax1.plot_surface(X, Y, Z_hat)
    surf2 = ax1.plot_surface(X, Y, Z)
    # Plotting the generated data
    # scatter = ax1.scatter(data_set['x'], data_set['y'], data_set['z'], c='r')

    # An attempt to visualise the error
    ax2 = f.add_subplot(1, 2, 2)
    #plt.pcolormesh(X, Y, -np.abs(Z_error), cmap=cm.RdYlGn)
    # Plot fitness over generations
    ax2.set_title('Fitness as function \nof generations')
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.plot(performance)

    plt.savefig('images_for_gif/generation' + str(generation))
    plt.close()

# Update loop
num_generations = 500
performance = []
for i in range(num_generations):
    calculate_fitness()
    gen_alg.next_generation(current_fitness)
    performance.append(gen_alg.best_fitness)
    c = gen_alg.best_decoded_chromosome
    save_my_fig(c, X, Y, i)
    #if i % 50 == 0:
    print("Generation: {}".format(i))