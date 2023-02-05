from ..binary_tree.node import Node


class SizeNode(Node):
    def __init__(self, item):
        super().__init__(item)
        self.size = 1

    def update(self):
        self.update_size()

    def update_size(self):
        self.size = 1 + subtree_size(self.left) + subtree_size(self.right)


def subtree_size(node: SizeNode) -> int:
    if node:
        return node.size
    return 0
