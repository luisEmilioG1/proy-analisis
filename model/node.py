import numpy as np
from collections import deque

from .estadoCanalF import EstadoCanalF

class Node:
    def __init__(self, id, estadosCanalF):
        self.id_channel = id
        self.EstadosCanalF = EstadoCanalF(np.array(estadosCanalF))
        self.deq = deque()

    def get_probability_distribution(self, index_combo: int):
        return self.EstadosCanalF.get_probability_distribution(index_combo)
    
    def marginalize_rows(self, tuple_index):
        return self.EstadosCanalF.marginalize_rows(tuple_index)

    def marginalize_rows_and_update(self, tuple_index):
        self.deq.append(self.EstadosCanalF)
        num_cols = len(self.EstadosCanalF.array)
        self.EstadosCanalF = self.EstadosCanalF.marginalize_rows(tuple_index).complete_array(num_cols, tuple_index)
        return self.EstadosCanalF

    def undo(self):
        self.EstadosCanalF = self.deq.pop()

    
        