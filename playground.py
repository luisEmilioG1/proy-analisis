import numpy as np

from model import Optimize
from model.util import distance, set_states_to_string, obtains_index_not_null
optimize = Optimize(
    [
    [1, 0],
    [1, 0],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1]
    ],
    [
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [0, 1],
    [1, 0],
    [0, 1],
    ],
    [
    [1, 0],
    [0, 1],
    [0, 1],
    [1, 0],
    [1, 0],
    [0, 1],
    [0, 1],
    [1, 0],
    ])

f_state=[True, True, True]
c_state=[1, None, 0]

num_characters_f_state = sum(1 for i in f_state if i is not None)
num_characters_c_state = sum(1 for i in c_state if i is not None)

index_not_null_f_state = [i for i in range(len(f_state)) if f_state[i] is not None]
index_not_null_c_state = [i for i in range(len(c_state)) if c_state[i] is not None]

count = num_characters_f_state + num_characters_c_state
initial_array = [0]*count
sol = float('inf')

def generate_all_partitions(charactersInPartition2, characterIndex=-1, changeCharacterToPartition2=False):
    global sol
    global f_state
    global c_state
    
    if sol == 0:
        return
    
    if changeCharacterToPartition2:
            charactersInPartition2[characterIndex] = 1

    if len(charactersInPartition2) == characterIndex+1:
        num_f = sum(charactersInPartition2)
        if num_f != 0 and num_f != len(charactersInPartition2):
            f_p1, c_p1, f_p2, c_p2 = array_to_partition(f_state, c_state, charactersInPartition2.copy())

            dist1 = optimize.get_probability_distribution(f_state=f_p1, c_state=c_p1)
            dist2 = optimize.get_probability_distribution(f_state=f_p2, c_state=c_p2)

            sol_comb = optimize._tensor_prod(dist2, dist1)
            soli = optimize.get_probability_distribution(f_state=f_state, c_state=c_state)

            height = distance(soli, sol_comb)
            if height < sol:
                sol = height
                i_fp1 = obtains_index_not_null(f_p1)
                i_cp1 = obtains_index_not_null(c_p1)
                i_fp2 = obtains_index_not_null(f_p2)
                i_cp2 = obtains_index_not_null(c_p2)

                
                print("-"*30)
                print("characters part 2: ",charactersInPartition2)
                print("p1: ","{ "+set_states_to_string(i_fp1)+ " | "+set_states_to_string(i_cp1)+" }")
                print("p2: ","{ "+set_states_to_string(i_fp2)+ " | "+set_states_to_string(i_cp2)+" }")
                print("original dist: ",soli)
                print("union distributions: ",sol_comb)
                print("distance: ", distance(soli, sol_comb))
                print("-"*30)
            return
    else:
        generate_all_partitions(charactersInPartition2.copy(), characterIndex + 1, False)
        generate_all_partitions(charactersInPartition2.copy(), characterIndex + 1, True)
 
    return

def array_to_partition(f_state, c_state, array):
    f_state_p1 = [None]*len(f_state)
    c_state_p1 = [None]*len(c_state)

    f_state_p2 = [None]*len(f_state)
    c_state_p2 = [None]*len(c_state)

    state_iterator = -1
    for i in range(len(array)):
        state_iterator += 1
        if i+1 <= num_characters_f_state:
            f_idex = index_not_null_f_state[state_iterator]
            if array[i]:
                f_state_p2[f_idex] = f_state[f_idex]
                f_state_p1[f_idex] = None
            else:
                f_state_p1[f_idex] = f_state[f_idex]
                f_state_p2[f_idex] = None    

            if i+1 == num_characters_f_state:
                state_iterator = -1    
        else:
            c_index = index_not_null_c_state[state_iterator]
            if array[i]:
                c_state_p2[c_index] = c_state[c_index]
                c_state_p1[c_index] = None
            else:
                c_state_p1[c_index] = c_state[c_index]
                c_state_p2[c_index] = None    
    
    return f_state_p1, c_state_p1, f_state_p2, c_state_p2
    
generate_all_partitions(initial_array)