# Genetic algorithm
One day I thought about fitting a surface to 3 dimensional data points, and solving this via a genetic algorithm seemed fitting. The reason I thought about this is that if one only has real valued features in a dataset one could just fit a polynomial with the number of variable of interest and then perform regression.
A standard genetic algortihm is implemented from "Biologically Inspired Optimization Methods: An Introduction" by Mattias Wadhe
using python, using roulette wheel selection, crossover and mutation.

# Task
An arbitrary bivariate function was constructed which the genetic algorithm will try to find the parameters of.

<img src="https://render.githubusercontent.com/render/math?math=f(x,y) = 2x^{2}-0.5y^{3}\+0.01x^{6}y-x^{4}y^{2}">

This surface can be seen as the orange surface in the gif below.

# Results
The algorithm got to evolve for 500 generations with a population size of 50 and a mutation probability of 0.02.
The results is that it works but it seems like a quite inefficient way to solve this problem. 
However a real number encoding instead of a binary encoding would probably increase the speed of the algorithm, 
alternatively writing the decoding functions in a faster language.

![Missing gif](gen_alg.gif)
