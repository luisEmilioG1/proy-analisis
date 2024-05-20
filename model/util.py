import math
import numpy as np
from pyphi.distance import _hamming_matrix, emd

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
    dist1 = np.array([float(i) for i in distribution1])
    dist2 = np.array([float(i) for i in distribution2])
    # TODO: check N value
    N = int(math.log2(len(dist1)))
    hamming_matrix = _hamming_matrix(N)
    return emd(dist1, dist2, hamming_matrix)

def get_character_by_index(index: int):
    return chr(index + 97).upper()

def set_channels_to_string(channels: set):
    channels_int = [get_character_by_index(int(i[1:])) for i in channels]
    channels_int.sort()
    return "".join(channels_int)