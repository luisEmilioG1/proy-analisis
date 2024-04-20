import numpy as np
from scipy.stats import wasserstein_distance

from model import Optimize

optimize = Optimize(
                [  
                    [1,	0],
                    [1,	0],
                    [0,	1],
                    [0,	1],
                ], 
                [   
                    [1,	0],
                    [1,	0],
                    [1,	0],
                    [1,	0],
                ]
            )
    
def generate_all_partitions(charactersInPartition2, characterIndex=-1, changeCharacterToPartition2=True, solutions=[]):
    if changeCharacterToPartition2:
            charactersInPartition2[characterIndex] = True
    print(charactersInPartition2)

    if True not in charactersInPartition2 or None not in charactersInPartition2: return

    union = tensor_prod(charactersInPartition2)
    distance = wasserstein_distance(initial_distribution, union)
    print(distance)
    if distance == 0.0:
         solutions.append(charactersInPartition2)

    if len(charactersInPartition2) == characterIndex+1: return

    else:
        if len(solutions) == 0:
            generate_all_partitions(charactersInPartition2.copy(), characterIndex + 1, False, solutions)
        if len(solutions) == 0:
            generate_all_partitions(charactersInPartition2.copy(), characterIndex + 1, True, solutions)
 
    return 

def tensor_prod(characters_partition2):
    characters_partition1 = [None if x else True for x in characters_partition2]

    future_state_p1 = characters_partition1[-len(optimize.estados_canal_f):]
    positions_current_state_p1 = characters_partition1[:len(c_state)]
    current_state_p1 = [c_state[i] if positions_current_state_p1[i] else None  for i in range(len(positions_current_state_p1))]

    future_state_p2 = characters_partition2[-len(optimize.estados_canal_f):]
    positions_current_state_p2 = characters_partition2[:len(c_state)]
    current_state_p2 = [c_state[i] if positions_current_state_p2[i] else None  for i in range(len(positions_current_state_p2))]

    distribution_p1 = optimize.get_probability_distribution(
                        c_state=current_state_p1, 
                        f_state=future_state_p1
                        )
    distribution_p2 = optimize.get_probability_distribution(
                        c_state=current_state_p2, 
                        f_state=future_state_p2
                        )
    return optimize._tensor_prod(distribution_p1, distribution_p2)
    
c_state=[0, 0]
global initial_distribution
initial_distribution= optimize.get_probability_distribution(c_state=c_state, f_state=[True, True])
initial_array = [None]*(len(optimize.estados_canal_f)*2)

solutions = []
generate_all_partitions(initial_array, solutions=solutions)
print(solutions)

# print("Número de combinaciones:", len(solutions))
# for characters_partition2 in solutions:
#     characters_partition1 = [None if x else True for x in characters_partition2]

#     future_state_p1 = characters_partition1[-len(optimize.estados_canal_f):]
#     positions_current_state_p1 = characters_partition1[:len(c_state)]
#     current_state_p1 = [c_state[i] if positions_current_state_p1[i] else None  for i in range(len(positions_current_state_p1))]

#     future_state_p2 = characters_partition2[-len(optimize.estados_canal_f):]
#     positions_current_state_p2 = characters_partition2[:len(c_state)]
#     current_state_p2 = [c_state[i] if positions_current_state_p2[i] else None  for i in range(len(positions_current_state_p2))]

#     print("current_state_p1: ",current_state_p1)
#     print("future_state_p1: ",future_state_p1)

#     #? calcule deitibutions idividual patitions
#     distribution_p1 = optimize.get_probability_distribution(
#                         c_state=current_state_p1, 
#                         f_state=future_state_p1
#                         )
#     print("distribution_p1: ",distribution_p1)
#     print("")


#     print("current_state_p2: ",current_state_p2)
#     print("future_state_p1: ",future_state_p2)
#     #! implementar cálculo con vacío
#     distribution_p2 = optimize.get_probability_distribution(
#                         c_state=current_state_p2, 
#                         f_state=future_state_p2
#                         )

#     print("distribution_p2: ",distribution_p2)

#     combinate = optimize._tensor_prod(distribution_p1, distribution_p2)
#     print("Conbinate distributions: ",combinate)
    
#     distance = wasserstein_distance([1, 0, 0, 0],combinate)
#     print("Wasserstein distance: ",distance)

#     print("-"*50)
