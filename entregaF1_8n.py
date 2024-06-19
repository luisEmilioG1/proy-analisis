from model import Graph
from datosentregaF.red1_8n import A, B, C, D, E, F, G, H
import time

start_time = time.time()
graph = Graph(A, B, C, D, E, F, G, H)

#?1 Futuro  = [A, B, C, D, E, F, G, H]   
#?  Presente= [A, B, C, D, E, F, G, H]	  
# graph.set_states(
#     next_state=[True, True, True, True, True, True, True, True],
#     current_state=[1, 0, 0, 0, 0, 0, 0, 0]
# )

#?2 Futuro = [A, B, C, G, H]
#?  Presente: [A, B, C, D, E, F, G, H]  
# graph.set_states(
#     next_state=[True, True, True, None, None, None, True, True],
#     current_state=[1, 0, 0, 0, 0, 0, 0, 0]
# )

#?3  Futuro = [A, B, C, D, E, F, G, H]
#?  Presente: [B, C, D, E, F, G, H]
# graph.set_states(
#     next_state=[True, True, True, True, True, True, True, True],
#     current_state=[None, 0, 0, 0, 0, 0, 0, 0]
# )

#?4  Futuro = [A, B, C, D, E, F, G, H]
#?   Presente: [D, E, F, G, H]
# graph.set_states(
#     next_state=[True, True, True, True, True, True, True, True],
#     current_state=[None, None, None, 0, 0, 0, 0, 0]
# )

#?5 Futuro = [A, B, C, D]
#?  Presente: [D, E, F, G, H]
graph.set_states(
    next_state=[True, True, True, True, None, None, None, None],
    current_state=[None, None, None, 0, 0, 0, 0, 0]
)

graph.optimize()
execution_time = time.time() - start_time
print("Execution time: ", execution_time, " seconds")
