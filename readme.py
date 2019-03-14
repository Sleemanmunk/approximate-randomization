# as seen in https://cs.stanford.edu/people/wmorgan/sigtest.pdf
import torch
import numpy as np
from recipes.approximate_randomization import chanceByChance, meangt, meandiff

A = np.random.rand(2, 10)
B = np.random.rand(1,10)*0.5
def show_eval(code):
    print(code, ":", eval(code))

# NOTE - approximate randomization is a stochastic test, so a small amount of variance is to be expected
# The chance that A[0] does not come from a distribution with a mean greater than that of A[1]
# (Default is meangt)
show_eval("chanceByChance(A[0],A[1])")
show_eval("chanceByChance(A[0],A[1],comparer=meangt)")  # identical functionality

show_eval("chanceByChance(A[0],B[0])")


# The chance that A[0] and A[1] come from the same distribution
show_eval("chanceByChance(A[0],A[1],comparer=meandiff)")
show_eval("chanceByChance(A[0],B[0],comparer=meandiff)")

# The chance that on average for a given x g(x) is not greater than f(x)
# when applied over the distribution represented by A[0]

def g(x): return x + 0.001
def f(x): return x

# Using regular approximate randomization the signal is overwhelmed by the noise
show_eval("chanceByChance(g(A[0]),f(A[0]),pairwise=False)")

# "pairwise" means we only swap matched pairs (e.g. A[0][i] and A[1][i]) when randomizing
show_eval("chanceByChance(g(A[0]),f(A[0]),pairwise=True)")