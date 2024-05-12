from .node import Node
from .combos import Combos

from .util import get_character_by_index

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

    def get_source_to_name(self) -> tuple:
        return ("c"+str(self.source.id_channel), "f"+str(self.to.id_channel))

    def __str__(self):
        return f'{get_character_by_index(self.source.id_channel)} -> {get_character_by_index(self.to.id_channel)}\''
    
        