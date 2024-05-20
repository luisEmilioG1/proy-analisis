from model import Graph
from data import estados_canalF1, estados_canalF2, estados_canalF3, estados_canalF4, estados_canalF5

graph = Graph(estados_canalF1, estados_canalF2, estados_canalF3, estados_canalF4, estados_canalF5)

# no partition
print("ABC|ABCD  = 1000")
graph.set_states(
    [1, 0, 0, 0, None], 
    [True, True, True, None, None]
)
graph.optimize()

for con in graph.connections:
    print(con)

index=[0, 4,7]
for i in index:
    graph.connections[i].cut(graph.combos)
print(graph.get_distance())
for i in index:
    graph.connections[i].undo()
