import numpy as np

from model import Optimize

optimize = Optimize(
                [  
                    [1,	0],
                    [1,	0],
                    [0,	1],
                    [0,	1],
                    [0,	1],
                    [0,	1],
                    [0,	1],
                    [0,	1],
                ], 
                [   
                    [1,	0],
                    [1,	0],
                    [1,	0],
                    [1,	0],
                    [1,	0],
                    [0,	1],
                    [1,	0],
                    [0,	1],
                ],
                [   
                    [1,	0],
                    [0,	1],
                    [0,	1],
                    [1,	0],
                    [1,	0],
                    [0,	1],
                    [0,	1],
                    [1,	0],
                ]
            )

for i in range(len(optimize.estados_canal_f[0].array)):
    acc_row = None
    for estado_canal_f in optimize.estados_canal_f:
        if acc_row is None:
            acc_row = estado_canal_f.array[i]
        else:
            acc_row = np.outer(estado_canal_f.array[i], acc_row).flatten()

    print(acc_row)
    