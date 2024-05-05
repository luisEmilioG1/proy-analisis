from .node import Node
from .combos import Combos

class Connection:
    def __init__(self, source: Node, to:Node):
        self.source = source
        self.to = to
        self.is_cut = False

    def cut(self, combos:Combos):
        index_channel_marginalize = self.source.id_channel

        marginalize_combos = combos.marginalize_combos([index_channel_marginalize])
        self.to.marginalize_rows_and_update(list(marginalize_combos.values()))

        self.is_cut = True

    def undo(self):
        self.to.undo()
        self.is_cut = False

    def __str__(self):
        return f'{self.source.id_channel} -> {self.to.id_channel}'
    
        