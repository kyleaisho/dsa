from trees.binary_tree.augment_bt_utils import insert
from .size_node import SizeNode


def test_node():
    root = SizeNode(7)

    assert root.size == 1


def test_after_insert():
    root = SizeNode(7)
    insert(root, 12)

    assert root.size == 2
    assert root.right.size == 1

    insert(root, 3)

    assert root.size == 3
    assert root.left.size == 1
    assert root.right.size == 1
