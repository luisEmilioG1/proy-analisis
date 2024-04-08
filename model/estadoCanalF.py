import numpy as np

class EstadoCanalF:
    def __init__(self, array: np.ndarray):
        """" array must be dimensions nX2 """
        self.array = array

    def marginalize_rows(self, index_rows_to_marginalize: list[list]) -> 'EstadoCanalF':
        new_array = None
        for group_index in index_rows_to_marginalize:

            acc_row = None
            for index in group_index:
                if acc_row is None:
                    acc_row = self.array.copy()[index]
                else:
                    acc_row = (acc_row + self.array.copy()[index]) /2
                
            if new_array is None:
                new_array = acc_row   
            else:
                new_array = np.vstack([new_array, acc_row])

        return EstadoCanalF(new_array)

    def get_probability_distribution(self, index_combo: int):
            return self.array[index_combo]

    def set_array(self, array: np.ndarray):
        self.array = array

