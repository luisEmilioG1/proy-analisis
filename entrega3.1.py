from model import Graph
from model import Optimize
from datosentrega3.channels6 import A, B, C, D, E, F
import time

start_time = time.time()
graph = Graph(A, B, C, D, E, F)

#?1 ABCDFt+1|ABCDFt
# graph.set_states(
#     next_state=[True, True, True, True, None, True],
#     current_state=[1, 0, 0, 0, None, 0]
# )

#?2 ABCDt+1|ABCDEFt
# graph.set_states(
#     next_state=[True, True, True, True, None, None],
#     current_state=[1, 0, 0, 0, 1, 0]
# )

#?3 ABCDEt+1|ABCDt
# graph.set_states(
#     next_state=[True, True, True, True, True, None],
#     current_state=[1, 0, 0, 0, None, None]
# )

#?4 ABCt+1|ABCDEt
# graph.set_states(
#     next_state=[True, True, True, None, None, None],
#     current_state=[1, 0, 0, 0, 1, None]
# )

#?5 ABCDEt+1|ABt
# graph.set_states(
#     next_state=[True, True, True, True, True, None],
#     current_state=[1, 0, None, None, None, None]
# )

#?6 ACDFt+1|ACDt
# graph.set_states(
#     next_state=[True, None, True, True, None, True],
#     current_state=[1, None, 0, 0, None, None]
# )

#?7 ABCt+1|ABCt
# graph.set_states(
#     next_state=[True, True, True, None, None, None],
#     current_state=[1, 0, 0, None, None, None]
# )

#?8 ABCEt+1|ABEt
# graph.set_states(
#     next_state=[True, True, True, None, True, None],
#     current_state=[1, 0, None, None, 1, None]
# )

#?9 BCFt+1|ABCt
# graph.set_states(
#     next_state=[None, True, True, None, None, True],
#     current_state=[1, 0, 0, None, None, None]
# )

#?10 BCt+1|CFt
# graph.set_states(
#     next_state=[None, True, True, None, None, None],
#     current_state=[None, None, 0, None, None, 0]
# )

#?11 ABCt+1|ACt
graph.set_states(
    next_state=[True, True, True, None, None, None],
    current_state=[1, None, 0, None, None, None]
)

graph.optimize()
execution_time = time.time() - start_time
print("Execution time: ", execution_time, " seconds")
