from model import Graph
from model import Optimize
from data import estados_canalF1, estados_canalF2, estados_canalF3, estados_canalF4, estados_canalF5
import time

start_time = time.time()
graph = Graph(estados_canalF1, estados_canalF2, estados_canalF3, estados_canalF4, estados_canalF5)


# - ABCD|ABCD     = 1000
# print("ABCD|ABCD    = 1000")
# graph.set_states(
#     [1, 0, 0, 0, None], 
#     [True, True, True, True, None]
# )
# graph.optimize()



# # - ABCD|ABCDE  = 10001
# print("ABCD|ABCDE  = 10001")
# graph.set_states(
#     [1, 0, 0, 0, 1], 
#     [True, True, True, True, None]
# )
# graph.optimize()


# # - ABCDE|ABCD  = 1000
# print("ABCDE|ABCD  = 1000")
# graph.set_states(
#     [1, 0, 0, 0, None], 
#     [True, True, True, True, True]
# )
# graph.optimize()

# # - ABC|ABCDE   = 10001
# print("ABC|ABCDE   = 10001")
# graph.set_states(
#     [1, 0, 0, 0, 1], 
#     [True, True, True, None, None]
# )
# graph.optimize()

# # - ABCDE|AB    =  10
print("ABCDE|AB    =  10")
graph.set_states(
    [1, 0, None, None, None], 
    [True, True, True, True, True]
)
graph.optimize()

execution_time = time.time() - start_time
print("Execution time: ", execution_time, " seconds")

