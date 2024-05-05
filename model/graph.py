from .node import Node
from .connection import Connection
from .combos import Combos
from .util import (
    obtains_index_not_null, 
    obtains_index_null,
    apply_formula,
    distance)

class Graph:

    def __init__(self, *estadosCanalF):
        self.nodes = {}
        self.connections = []
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

    def is_bipartition(self) -> bool:
        # TODO
        pass

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
        print("old: ", self.initial_probability_distribution)
        print("new: ", new_probability_distribution)
        return distance(self.initial_probability_distribution, new_probability_distribution)

    def optimize(self):
        for connection in self.connections:        
            print(connection.__str__())
            con = connection.__str__()
            connection.cut(self.combos)
            distance = self.get_distance()
            print("distance: ",distance)

            if distance > 0:
                connection.undo()

            print("-"*30)
        print()
