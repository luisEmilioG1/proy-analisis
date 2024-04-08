from .estadoCanalF import EstadoCanalF
from .combos import Combos
from .util import obtains_index_null, obtains_index_not_null

import numpy as np

class Optimize:
    def __init__(self, *estadosCanalF):
        """" every one array estadosCanalF must be dimensions nX2 """
        self.estados_canal_f = [EstadoCanalF(np.array(array)) for array in estadosCanalF]
        self.combos = Combos(len(self.estados_canal_f))

    def get_probability_distribution(self, c_state:list, f_state:list):
        index_channels_in_future = obtains_index_not_null(f_state)
        index_channels_in_present = obtains_index_not_null(c_state)

        index_channels_not_in_present = obtains_index_null(c_state)

        # case no marginalize present
        # TODO: use table EstadosEstadoF
        if len(index_channels_in_present) == len(self.estados_canal_f):     
            c_state_str = ''.join(map(str, c_state))       
            index_combo_current_state = self.combos.get_index_combo(c_state_str)
            probability_distributions = [self.estados_canal_f[i].get_probability_distribution(index_combo_current_state) for i in index_channels_in_future]
            return self._apply_formula(probability_distributions)
        
        # case marginalize present
        else:
            c_state_not_null = list(filter(lambda x: x is not None, c_state))
            c_state_str = ''.join(map(str, c_state_not_null))

            new_combos = Combos(len(index_channels_in_present))
            index_combo_current_state = new_combos.get_index_combo(c_state_str) 

            marginalize_combos = self.combos.marginalize_combos(index_channels_not_in_present)
            probability_distributions = [self.estados_canal_f[i].marginalize_rows(list(marginalize_combos.values())).get_probability_distribution(index_combo_current_state) for i in index_channels_in_future]

            return self._apply_formula(probability_distributions)

    def _tensor_prod(self, distribution1: list, distribution2:list):        
        return np.outer(distribution1, distribution2).flatten()

    def _apply_formula(self, probability_distributions: list):
        distribution_result = None
        for distribution in probability_distributions:
            if distribution_result is None:
                distribution_result = distribution
            else:
                distribution_result = self._tensor_prod(distribution, distribution_result)

        return distribution_result

