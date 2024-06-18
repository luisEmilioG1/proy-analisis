from model import Graph
from model import Optimize
from datosentregaF.red_6n import A, B, C, D, E, F
import time

start_time = time.time()
graph = Graph(A, B, C, D, E, F)

#?11 ABCt+1|ACt
graph.set_states(
    next_state=[True, True, True, None, None, None],
    current_state=[1, None, 0, None, None, None]
)

graph.optimize()
execution_time = time.time() - start_time
print("Execution time: ", execution_time, " seconds")
