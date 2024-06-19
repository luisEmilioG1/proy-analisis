from model import Graph
from datosentregaF.red_10n import A, B, C, D, E, F, G, H, I, J
import time

start_time = time.time()
graph = Graph(A, B, C, D, E, F, G, H, I, J)

#? 1) ABCDEFGHIJt+1|ABCDEFGHIJt
# graph.set_states(
#     next_state=[True, True, True, True, True, True, True, True, True, True],
#     current_state=[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# )

#? 2) ABCDEFJt+1|ABCDEFGHIJt
# graph.set_states(
#     next_state=[True, True, True, True, True, True, None, None, None, True],
#     current_state=[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# )

#? 3) ABCDEFJt+1|ADEFGHIJt
# graph.set_states(
#     next_state=[True, True, True, True, True, True, None, None, None, True],
#     current_state=[1, None, None, 0, 0, 0, 0, 0, 0, 0]
# )

#? 4) ABCDEFGJ | ABDEFGHIJ
# graph.set_states(
#     next_state=[True, True, True, True, True, True, True, None, None, True],
#     current_state=[1, 0, None, 0, 0, 0, 0, 0, 0, 0]
# )
 
#? 5) ADEFGJ | ABDEJ
# graph.set_states(
#     next_state=[True, None, None, True, True, True, True, None, None, True],
#     current_state=[1, 0, None, 0, 0, None, None, None, None, 0]
# )

#? 6) ABDEFGJ | ABDEIJ
graph.set_states(
    next_state=[True, True, None, True, True, True, True, None, None, True],
    current_state=[1, 0, None, 0, 0, None, None, None, 0, 0]
)
graph.optimize()

execution_time = time.time() - start_time
print("Execution time: ", execution_time, " seconds")
