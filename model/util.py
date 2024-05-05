import numpy as np
from scipy.stats import wasserstein_distance

def obtains_index_not_null(elements_list: list):
    return [i for i, x in enumerate(elements_list) if x is not None]

def obtains_index_null(elements_list: list):
    return [i for i, x in enumerate(elements_list) if x is None]

def tensor_prod(distribution1: list, distribution2:list):        
    return np.outer(distribution1, distribution2).flatten()

def apply_formula(probability_distributions: list):
    distribution_result = None
    for distribution in probability_distributions:
        if distribution_result is None:
            distribution_result = distribution
        else:
            distribution_result = tensor_prod(distribution, distribution_result)

    return distribution_result

def distance(distribution1: list, distribution2: list):
    return wasserstein_distance(distribution1, distribution2)