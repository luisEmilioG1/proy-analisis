import numpy as np
from red_6n import EstadoEstadoF

def marginalize_cols(index_to_sum, estado_estadoF):
    # [(1,2,4), (0,3,5)]
    table = np.array(estado_estadoF)
    sol = None
    col_0 = None
    for tup in index_to_sum:
        for i in tup:
            if col_0 is None:
                col_0 = table[:, i]
            else:
                col_0 = col_0+ table[:, i]
        if sol is None:
            sol = np.array(col_0[:, None])
        else:
            sol = np.hstack((sol, col_0[:, None]))
        col_0 = None
    print(sol)

def generate_index_to_sum(n, channel):
    combos = generate_combos(channel)
    
    tup0 = []
    tup1 = []

    for i in combos:
        if i[n] == '0':
            tup0.append(combos.index(i))
        else:
            tup1.append(combos.index(i))
    
    return [tup0, tup1]

def generate_combos(n: int):
        combos = []
        for i in range(2**n):
            binary = bin(i)[2:]
            binary = '0'*(n-len(binary)) + binary
            binary = binary[::-1]
            combos.append(binary)

        return combos

for i in range(6):
    marginalize_cols(generate_index_to_sum(i, 6), EstadoEstadoF)