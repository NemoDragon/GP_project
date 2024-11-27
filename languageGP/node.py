class Node:
    def __init__(self, node_type, value=None, children=None):
        self.node_type = node_type
        self.value = value
        self.children = children or []

    def __repr__(self, level=0):
        indent = "  " * level
        repr_str = f"{indent}{self.node_type}({self.value})\n"
        for child in self.children:
            repr_str += child.__repr__(level + 1)
        return repr_str