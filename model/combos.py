from math import log2

class Combos:

    def __init__(self, num_channels:int):
        self.combos = self._generate_combos(num_channels)

    def get_index_combo(self, combo):
        return self.combos[combo]

    def _generate_combos(self, n: int) -> dict[str, int]:
        combos = {}

        for i in range(2**n):
            binary = bin(i)[2:]
            binary = '0'*(n-len(binary)) + binary
            binary = binary[::-1]
            combos[binary] = i

        return combos
    
    def marginalize_combos(self, index_channels_to_marginalize: list[int]) -> dict[str, int]:
        new_combos = {}
        for combo_key in self.combos.keys():
            new_combo = ''
            for index_byte in range(len(combo_key)):
                if index_byte not in index_channels_to_marginalize:
                    new_combo = new_combo + combo_key[index_byte]
            if new_combo not in new_combos:
                new_combos[new_combo] = [list(self.combos.keys()).index(combo_key)]
            else:
                new_combos[new_combo].append(list(self.combos.keys()).index(combo_key))

        return new_combos