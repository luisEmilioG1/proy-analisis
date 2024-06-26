from .estadoCanalF import EstadoCanalF
from .estadoEstadoF import EstadoEstadoF
from .combos import Combos
from .util import obtains_index_null, obtains_index_not_null

import numpy as np

class Optimize:
    def __init__(self, *estadosCanalF):
        """" every one array estadosCanalF must be dimensions nX2 """
        self.estados_canal_f = [EstadoCanalF(np.array(array)) for array in estadosCanalF]
        self.combos = Combos(len(self.estados_canal_f))
        self.estado_estado_f = EstadoEstadoF(self._generate_EstadoEstadoF())

    def get_probability_distribution(self, c_state:list, f_state:list):
        index_channels_in_future = obtains_index_not_null(f_state)
        index_channels_in_present = obtains_index_not_null(c_state)

        index_channels_not_in_present = obtains_index_null(c_state)

        # empty future
        if len(index_channels_in_future) == 0 :
            return [1]
        
        if len(index_channels_in_present) == 0:
            x = 1/(len(index_channels_in_future)*2)
            return [x]*(2**len(index_channels_in_future))

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

            dist_to_combine = []
            for i in index_channels_in_future:
                estados_canal_f = self.estados_canal_f[i]
                num_channels_available = len(c_state)
                for c in range(len(index_channels_not_in_present)-1, -1, -1):
                    channel = index_channels_not_in_present[c]
                    new_combos = Combos(num_channels_available)
                    marginalize_combos = new_combos.marginalize_combos([channel])
                    
                    estados_canal_f = estados_canal_f.marginalize_rows(list(marginalize_combos.values()))
                    num_channels_available -= 1
                dist_to_combine.append(estados_canal_f.get_probability_distribution(index_combo_current_state))

            return self._apply_formula(dist_to_combine)

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

    def _generate_EstadoEstadoF(self):
        estado_estado_f = []
        for i in range(len(self.estados_canal_f[0].array)):
            acc_row = None
            for estado_canal_f in self.estados_canal_f:
                if acc_row is None:
                    acc_row = estado_canal_f.array[i]
                else:
                    acc_row = np.outer(estado_canal_f.array[i], acc_row).flatten()
            estado_estado_f.append(acc_row)
        return estado_estado_f