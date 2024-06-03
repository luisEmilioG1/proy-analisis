import math
import numpy as np
from pyphi.distance import _hamming_matrix, emd

dist1 = np.array([.0, .5, .25, .25])
dist2 = np.array([.25, .25, .25, .25])

N = int(2)
hamming_matrix = _hamming_matrix(N)
print(hamming_matrix)
print(emd(dist1, dist2, hamming_matrix))