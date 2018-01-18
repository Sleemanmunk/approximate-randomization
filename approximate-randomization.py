import numpy as np

def meandiff(sample1,sample2):
    mean1 = np.mean(sample1)
    mean2 = np.mean(sample2)
    diff = abs(mean1-mean2)
    return diff

#Return the likelihood that sample1's mean is different than sample2's merely by chance
def chanceByChance(sample1,sample2,comparer=None,pairwise=True,repetitions=10000):
    if not comparer:
        comparer = meandiff
    true_diff = comparer(sample1,sample2)

    n = len(sample1)
    m = len(sample2)

    if pairwise and n != m:
        raise Exception("samples must be same size for pairwise. Got sample sizes {} and {}".format(n,m))

    combined = np.concatenate([sample1,sample2])

    def run_test(_):
        np.random.shuffle(combined)
        diff = comparer(combined[:n],combined[n:])
        return diff > true_diff

    def run_pairwise_test(_):
        swapper = np.random.rand(n)<0.5
        s1new = np.select([swapper,~swapper],[sample1,sample2])
        s2new = np.select([swapper,~swapper],[sample2,sample1])
        diff = comparer(s1new,s2new)
        return diff >= true_diff

    test = run_pairwise_test if pairwise else run_test

    results = map(test,range(repetitions))

    return (sum(results)+1)/(repetitions+1)
