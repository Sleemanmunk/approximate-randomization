# approximate-randomization
An implementation of the Approximate Randomization test in python

Also known as a "permutation test"

Algorithm: https://cs.stanford.edu/people/wmorgan/sigtest.pdf

## Example
NOTE - approximate randomization is a stochastic test, so a small amount of variance is to be expected
```
from approximate-randomization import *
A = np.random.rand(2, 10)
B = np.random.rand(1,10)*0.5
```
The chance that A[0] does not come from a distribution with a mean greater than that of A[1]


```
chanceByChance(A[0],A[1]) # 0.8509149085091491
chanceByChance(A[0],B[0]) # 0.0400959904009599

#Identical functionality
chanceByChance(A[0],A[1],comparer=meangt) # 0.8522147785221478
```

The chance that A[0] and A[1] come from the same distribution
```
chanceByChance(A[0],A[1],comparer=meandiff) # 0.29127087291270876
chanceByChance(A[0],B[0],comparer=meandiff) # 0.08099190080991901
```

The chance that on average for a given x `g(x)` is not greater than `f(x)`
when applied over the distribution represented by `A[0]`
```
def g(x): return x + 0.001
def f(x): return x

# Using regular approximate randomization the signal is overwhelmed by the noise
chanceByChance(g(A[0]),f(A[0]),pairwise=False) # 0.49595040495950404

# "pairwise" means we only swap matched pairs (e.g. A[0][i] and A[1][i]) when randomizing
chanceByChance(g(A[0]),f(A[0]),pairwise=True) # 0.0012998700129987
```


see readme.py to try these examples out

