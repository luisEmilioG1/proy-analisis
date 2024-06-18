from model import Graph
from datosentregaF.red1_8n import A, B, C, D, E, F, G, H
import time

start_time = time.time()
graph = Graph(A, B, C, D, E, F, G, H)

#?11 ABCt+1|ACt
graph.set_states(
    next_state=[True, True, True, None, None, None, True, True],
    current_state=[1, None, 0, None, None, None, 0, 0]
)

graph.optimize()
execution_time = time.time() - start_time
print("Execution time: ", execution_time, " seconds")
