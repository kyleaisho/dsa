from dsa.trees.binary_tree.node import Node


def test_node():
    root = Node(7)
    assert root.item == 7
    assert root.left == None
    assert root.right == None
    assert root.parent == None
