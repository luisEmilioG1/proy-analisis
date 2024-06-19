from model import Graph
from model import Optimize
from datosentregaF.red_6n import A, B, C, D, E, F
import time

start_time = time.time()
graph = Graph(A, B, C, D, E, F)

#? 1)ABCt+1|ACt
# graph.set_states(
#     next_state=[True, True, True, None, None, None],
#     current_state=[1, None, 0, None, None, None]
# )

#? 2)ABCt+1|ABCt
# graph.set_states(
#     next_state=[True, True, True, None, None, None],
#     current_state=[1, 0, 0, None, None, None]
# )

#? 3)ABCt+1|ABCDEt
# graph.set_states(
#     next_state=[True, True, True, None, None, None],
#     current_state=[1, 0, 0, 0, 0, None]
# )

#? 4)ABCt+1|ABCEt
# graph.set_states(
#     next_state=[True, True, True, None, None, None],
#     current_state=[1, 0, 0, None, 0, None]
# )

#? 5)ABCt+1|ACDEt
# graph.set_states(
#     next_state=[True, True, True, None, None, None],
#     current_state=[1, None, 0, 0, 0, None]
# )

#? 6)ABCt+1|ACDEFt
# graph.set_states(
#     next_state=[True, True, True, None, None, None],
#     current_state=[1, None, 0, 0, 0, 0]
# )

#? 7)BCDEFt+1|ABEFt
graph.set_states(
    next_state=[None, True, True, True, True, True],
    current_state=[1, 0, None, None, 0, 0]
)

graph.optimize()
execution_time = time.time() - start_time
print("Execution time: ", execution_time, " seconds")
