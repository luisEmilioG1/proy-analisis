from .node import Node
from .connection import Connection
from .combos import Combos
from .util import (
    obtains_index_not_null, 
    set_channels_to_string,
    obtains_index_null,
    apply_formula,
    distance)

class Graph:

    def __init__(self, *estadosCanalF):
        self.nodes:dict[int, Node] = {}
        self.connections:list[Connection] = []

        self.nodes_bipartition_representation = set([])
        self.connections_bipartition_representation = {}

        for i in range(len(estadosCanalF)):
            self.add_node(i, estadosCanalF[i])

        self.combos = Combos(len(estadosCanalF))

    def add_node(self, i, estadoCanalF):
        self.nodes[i] = Node(i, estadoCanalF)

    def set_states(self, current_state, next_state):
        self.current_state = current_state
        self.next_state = next_state

        index_channels_in_future = obtains_index_not_null(next_state)
        index_channels_in_present = obtains_index_not_null(current_state)

        # update connections
        for channel_future in index_channels_in_future:
            for channel_present in index_channels_in_present:
                if channel_present != channel_future:
                    self.add_connection(channel_present, channel_future)

        self.initial_probability_distribution = self.get_probability_distribution()

    def add_connection(self, source, to):
        new_connection = Connection(self.nodes[source], self.nodes[to])
        self.connections.append(new_connection)

    def cut(self, connection):
        connection.cut()

    def undo(self, connection):
        connection.undo()

    def is_bipartition(self, to) -> bool:
        adjacent = []
        queue = [to]
        while queue:
            u = queue.pop(0)
            if u not in self.connections_bipartition_representation:
                return True
            else:
                adjacent.append(u)
                for v in self.connections_bipartition_representation[u]:
                    if v not in adjacent and v not in queue:
                        queue.append(v)

        return len(adjacent) != len(self.nodes_bipartition_representation)

    def get_probability_distribution(self):
        index_channels_in_future = obtains_index_not_null(self.next_state)
        index_channels_in_present = obtains_index_not_null(self.current_state)

        index_channels_not_in_present = obtains_index_null(self.current_state)

        # empty future
        if len(index_channels_in_future) == 0 :
            return [1]
        
        if len(index_channels_in_present) == 0:
            x = 1/(len(index_channels_in_future)*2)
            return [x]*(2**len(index_channels_in_future))

        # case no marginalize present
        if len(index_channels_in_present) == len(self.nodes):     
            c_state_str = ''.join(map(str, self.current_state))       
            index_combo_current_state = self.combos.get_index_combo(c_state_str)
            probability_distributions = [self.nodes[i].get_probability_distribution(index_combo_current_state) for i in index_channels_in_future]
            return apply_formula(probability_distributions)
        
        # case marginalize present
        else:
            c_state_not_null = list(filter(lambda x: x is not None, self.current_state))
            c_state_str = ''.join(map(str, c_state_not_null))

            new_combos = Combos(len(index_channels_in_present))
            index_combo_current_state = new_combos.get_index_combo(c_state_str) 

            marginalize_combos = self.combos.marginalize_combos(index_channels_not_in_present)
            probability_distributions = [self.nodes[i].marginalize_rows(list(marginalize_combos.values())).get_probability_distribution(index_combo_current_state) for i in index_channels_in_future]

            return apply_formula(probability_distributions)

    def get_distance(self):
        new_probability_distribution = self.get_probability_distribution()
        #print("old: ", self.initial_probability_distribution)
        #print("new: ", new_probability_distribution)
        return distance(self.initial_probability_distribution, new_probability_distribution)

    def update_nodes_bipartition_representation(self):
        self.nodes_bipartition_representation = set([])
        for connection in self.connections:
            if not connection.is_cut:
                source, to = connection.get_source_to_name()
                self.nodes_bipartition_representation.add(source)
                self.nodes_bipartition_representation.add(to)

    def update_connections_bipartition_representation(self):
        self.connections_bipartition_representation = {}
        for connection in self.connections:
            source, to = connection.get_source_to_name()

            if to not in self.connections_bipartition_representation:
                    self.connections_bipartition_representation[to] = set([])
            
            if source not in self.connections_bipartition_representation:
                    self.connections_bipartition_representation[source] = set([])

            if not connection.is_cut:
                self.connections_bipartition_representation[to].add(source)
                self.connections_bipartition_representation[source].add(to)

    def optimize(self):
        self.update_nodes_bipartition_representation()
        bipartition = False
        i = 0
        while not bipartition and i < len(self.connections):        
            connection = self.connections[i]
            # print(connection.__str__())
            con = connection.__str__()
            connection.cut(self.combos)
            distance = self.get_distance()
            connection.set_loss(distance)
            # print("distance: ",distance)

            if distance > 0:
                connection.undo()
            else:
                _, to = connection.get_source_to_name()
                self.update_connections_bipartition_representation()
                bipartition = self.is_bipartition(to)
            i += 1
            # print("-"*30)

        if bipartition:
            self.sol_to_string()
            print("loss value: ", 0.0)
            print(self.get_probability_distribution())
        else:
            self.strategy()
        
    def sol_to_string(self):
        current_partition1 = set([])
        future_partition1 = set([])
        current_partition2 = set([])
        future_partition2 = set([])
        for sol_conn in list(self.connections_bipartition_representation.keys()):
            if sol_conn.startswith("f"):
                continue
            if len(current_partition1) == 0:
                current_partition1.add(sol_conn)
                future_partition1= future_partition1.union(self.connections_bipartition_representation[sol_conn])
            elif future_partition1 & self.connections_bipartition_representation[sol_conn]:
                current_partition1.add(sol_conn)
                future_partition1 = future_partition1.union(self.connections_bipartition_representation[sol_conn])
            else:
                current_partition2.add(sol_conn)
                future_partition2 = future_partition2.union(self.connections_bipartition_representation[sol_conn])

        for sol_conn in list(self.connections_bipartition_representation.keys()):
            if sol_conn.startswith("c"):
                continue   
            if sol_conn not in future_partition1:
                future_partition2 = future_partition2.union([sol_conn])
            if sol_conn not in future_partition2:
                future_partition1 = future_partition1.union([sol_conn])
            

        print("P1= {",
               set_channels_to_string(future_partition1),
               "|",
               set_channels_to_string(current_partition1),
               "}"
               )
        print("P2= {",
               set_channels_to_string(future_partition2),
               "|",
               set_channels_to_string(current_partition2)
                ,"}"
               )

    def strategy(self):
        global_level = float('inf')
        sol = None
        dist = None
        def wrapper(i=0):
            nonlocal global_level
            nonlocal sol
            nonlocal dist

            connection = self.connections[i]
            if connection.is_cut:
                return
            connection.cut(self.combos)
            distance = self.get_distance()

            _, to = connection.get_source_to_name()
            self.update_connections_bipartition_representation()
            
            if self.is_bipartition(to) and distance < global_level:                 
                global_level = distance
                sol = self.connections_bipartition_representation.copy()
                dist = self.get_probability_distribution().copy()
            elif distance < global_level:
                for i in range(len(self.connections)):
                    conn = self.connections[i]
                    if not conn.is_cut:
                        wrapper(i)

            connection.undo()
        
        for i in range(len(self.connections)):
            wrapper(i)
        
        self.connections_bipartition_representation = sol
        self.sol_to_string()
        print("loss value: ", global_level)
        print(dist)
        