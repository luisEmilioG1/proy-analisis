from model import Graph
from model import Optimize
from data import estados_canalF1, estados_canalF2, estados_canalF3, estados_canalF4, estados_canalF5
import time

start_time = time.time()
graph = Graph(estados_canalF1, estados_canalF2, estados_canalF3, estados_canalF4, estados_canalF5)

graph.set_states(
    [1, 0, 0, 0, 1], 
    [True, True, True, True, True]
)

graph.optimize()
execution_time = time.time() - start_time
print("Execution time: ", execution_time, " seconds")

print("-"*30,"\n")

opt = Optimize(estados_canalF1, estados_canalF2, estados_canalF3, estados_canalF4, estados_canalF5)


# - ABCD|ABCD     = 1000
start_time = time.time()
print("ABCD|ABCD    = 1000")
print(opt.get_probability_distribution(
    c_state=[1, 0, 0, 0, None], 
    f_state=[True, True, True, True, None]
))

# # - ABCD|ABCDE  = 10001
print("ABCD|ABCDE  = 10001")
print(opt.get_probability_distribution(
    c_state=[1, 0, 0, 0, 1], 
    f_state=[True, True, True, True, None]
))


# # - ABCDE|ABCD  = 1000
print("ABCDE|ABCD  = 1000")
print(opt.get_probability_distribution(
    c_state=[1, 0, 0, 0, None], 
    f_state=[True, True, True, True, True]
))

# # - ABC|ABCDE   = 10001
print("ABC|ABCDE   = 10001")
print(opt.get_probability_distribution(
    c_state=[1, 0, 0, 0, 1], 
    f_state=[True, True, True, None, None]
))

# # - ABCDE|AB    =  10
print("ABCDE|AB    =  10")
print(opt.get_probability_distribution(
    c_state=[1, 0, None, None, None], 
    f_state=[True, True, True, True, True]
)) 

execution_time = time.time() - start_time
print("Execution time: ", execution_time, " seconds")