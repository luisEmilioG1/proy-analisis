from model import Graph
from model import Optimize
from datosentregaF.red_4n import A, B, C, D
import time

start_time = time.time()
graph = Graph(A, B, C, D)

#?11 ABCt+1|ACt
graph.set_states(
    next_state=[None, True, True, None],
    current_state=[1, 0, 0, None]
)

graph.optimize()
execution_time = time.time() - start_time
print("Execution time: ", execution_time, " seconds")
