from model import Graph
from model import Optimize
from datosentregaF.red_4n import A, B, C, D
import time

start_time = time.time()
graph = Graph(A, B, C, D)

#? 1) ABCDt+1|ABCDt
# graph.set_states(
#     next_state=[True, True, True, True],
#     current_state=[1, 0, 0, 0]
# )

#? 2) ABCt+1|ABCDt
# graph.set_states(
#     next_state=[True, True, True, None],
#     current_state=[1, 0, 0, 0]
# )

#? 3) ABCDt+1|ACt
# graph.set_states(
#     next_state=[True, True, True, True],
#     current_state=[1, None, 0, None]
# )

#? 4) ACt+1|ABCt
# graph.set_states(
#     next_state=[True, None, True, None],
#     current_state=[1, 0, 0, None]
# )

#? 5) ABCt+1|ABCt
graph.set_states(
    next_state=[True, True, True, None],
    current_state=[1, 0, 0, None]
)

graph.optimize()
execution_time = time.time() - start_time
print("Execution time: ", execution_time, " seconds")
