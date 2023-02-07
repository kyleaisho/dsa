from .size_node import SizeNode
from .augment_bt_utils import rotate_if_needed


class AVLNode(SizeNode):
    def update(self):
        super().update()
        rotate_if_needed(self)
