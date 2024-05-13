from model import Graph
from model import Optimize

graph = Graph(
                [  
                    [0,	1],
                    [0,	1],
                    [1,	0],
                    [1,	0],
                    [1,	0],
                    [1,	0],
                    [1,	0],
                    [1,	0],
                ], 
                [   
                    [0,	1],
                    [0,	1],
                    [0,	1],
                    [0,	1],
                    [0,	1],
                    [1,	0],
                    [0,	1],
                    [1,	0],
                ],
                [   
                    [0,	1],
                    [1,	0],
                    [1,	0],
                    [0,	1],
                    [0,	1],
                    [1,	0],
                    [1,	0],
                    [0,	1],
                ]
            )

optimize = Optimize(
     [[0.5, 0.5],
       [0.5, 0.5],
       [1. , 0. ],
       [1. , 0. ],
       [0.5, 0.5],
       [0.5, 0.5],
       [1. , 0. ],
       [1. , 0. ]], 
                [[0. , 1. ],
       [0. , 1. ],
       [0. , 1. ],
       [0. , 1. ],
       [0.5, 0.5],
       [0.5, 0.5],
       [0.5, 0.5],
       [0.5, 0.5]],
                [   
                    [0,	1],
                    [1,	0],
                    [1,	0],
                    [0,	1],
                    [0,	1],
                    [1,	0],
                    [1,	0],
                    [0,	1],
                ]
)

graph.set_states(
    [0, 1, 0], 
    [True, True, True]
)
graph.optimize()

print(graph.initial_probability_distribution)
# print([node.EstadosCanalF.array for node in list(graph.nodes.values())])
print(optimize.get_probability_distribution(
    [0, 1, 0], 
    [True, True, True]
))
# [0 0 1 0 0 0 0 0]

# p1 = optimize.get_probability_distribution(
#     [0, None, 0], 
#     [True, True, None]
# )

# p2 = optimize.get_probability_distribution(
#     [None, 1, None], 
#     [None, None, True]
# )

# print(p1, p2)