from trees.binary_tree import BinaryTreeNode, build_binary_tree

def test_binary_tree_node():
    node = BinaryTreeNode(7)

    assert node.item == 7
    assert node.left is None
    assert node.right is None
    assert node.parent is None

def test_insert():
    root = BinaryTreeNode(7)
    assert root.height == 0
    
    root.insert(6)
    assert root.height == 1
    
    root.insert(8)
    assert root.height == 1

    root.insert(10)
    assert root.height == 2

    assert root.item == 7
    assert root.left.item == 6
    assert root.right.item == 8

def test_build():
    values = [7,6,3,2,9,10]
    root = build_binary_tree(values)

    assert root.item == 7
    assert root.left.item == 6
    assert root.right.item == 9

    assert root.left.left.item == 3
    assert root.right.right.item == 10

    assert root.left.left.left.item == 2

def test_find():
    values = [7,6,3,2,9,10]
    root = build_binary_tree(values)

    assert root.find(7) == root
    assert root.find(6) == root.left
    assert root.find(9) == root.right
    assert root.find(10) == root.right.right
    assert root.find(2) == root.left.left.left

def test_find_item_not_in_tree():
    values = [7,6,3,2,9,10]
    root = build_binary_tree(values)

    assert root.find(8) == None


def test_min():
    values = [7,6,3,2,9,10]
    root = build_binary_tree(values)

    assert root.get_min().item == 2
    assert root.right.get_min().item == 9
    assert root.left.get_min().item == 2


def test_max():
    values = [7,6,3,2,9,10]
    root = build_binary_tree(values)

    assert root.get_max().item == 10
    assert root.left.get_max().item == 6

def test_successor():
    values = [7,6,3,2,9,10]
    root = build_binary_tree(values)

    assert root.successor() == root.find(9)
    assert root.right.successor() == root.find(10)
    assert root.right.right.successor() == None

    assert root.find(6).successor() == root
    assert root.find(3).successor() == root.find(6)
    assert root.find(2).successor() == root.find(3)

def test_predecessor():
    values = [7,6,3,2,9,10]
    root = build_binary_tree(values)

    assert root.predecessor() == root.find(6)
    assert root.left.predecessor() == root.find(3)
    assert root.left.left.left.predecessor() == None

    assert root.right.predecessor() == root
    assert root.right.right.predecessor() == root.right

def test_find_next():
    values = [7,6,3,2,9,10]
    sorted_values = values[:]
    sorted_values.sort()
    root = build_binary_tree(values)

    assert root.find_next(8) == root.find(9)
    assert root.find_next(1) == root.find(2)
    assert root.find_next(7) == root.find(9)
    assert root.find_next(10) == None

    # validate against a sorted array
    for idx, val in enumerate(sorted_values):
        if idx < len(sorted_values) - 1:
            next_val = sorted_values[idx + 1]
            assert root.find_next(val).item == next_val
        else:
            root.find_next(val) == None

def test_find_prev():
    values = [7,6,3,2,9,10]
    sorted_values = values[:]
    sorted_values.sort()
    root = build_binary_tree(values)

    assert root.find_prev(8) == root
    assert root.find_prev(2) == None
    assert root.find_prev(1) == None
    assert root.find_prev(7) == root.find(6)
    assert root.find_prev(10) == root.find(9)

    # validate against a sorted array
    for idx, val in enumerate(sorted_values):
        if idx > 0:
            prev_val = sorted_values[idx - 1]
            assert root.find_prev(val).item == prev_val
        else:
            root.find_prev(val) == None

