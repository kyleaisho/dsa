from ..binary_tree.node import Node


class SizeNode(Node):
    def __init__(self, item):
        super().__init__(item)
        self.size = 1
        self.height = 0

    def update(self):
        self.update_size()
        self.update_height()

    def update_size(self):
        self.size = 1 + subtree_size(self.left) + subtree_size(self.right)

    def update_height(self):
        self.height = 1 + max(subtree_height(self.right), subtree_height(self.left))

    @property
    def skew(self):
        return subtree_height(self.right) - subtree_height(self.left)


def subtree_size(node: SizeNode) -> int:
    if node:
        return node.size
    return 0


def subtree_height(node: SizeNode) -> int:
    if node:
        return node.height
    return -1
