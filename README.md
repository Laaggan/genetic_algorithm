# Genetic algorithm
I thought about fitting a surface to 3 dimensional data points, and solving this via a genetic algorithm seemed fitting. 
A standard genetic algortihm is implemented from "Biologically Inspired Optimization Methods: An Introduction" by Mattias Wadhe
using python. The algorithm got to evolve for 500 generations with a population size of 50 and a mutation probability of 0.02

# Results
The results is that it works but it seems like a quite inefficient way to solve this problem. 
However a real number encoding instead of a binary encoding would probably increase the speed of the algorithm, 
alternatively writing the decoding functions in a faster language.

![Missing gif](gen_alg.gif)
