from ..bst.binary_search_tree import insert, build_bst


def test_insert():
    root = insert(None, 7)
    insert(root, 6)

    assert root.left.item == 6
    assert root.right == None

    insert(root, 6)
    assert root.left.left.item == 6

    insert(root, 9)
    assert root.right.item == 9

    insert(root, 8)
    assert root.right.left.item == 8


def test_build():
    items = [10, 4, 16, 5, 17, 21, 1]
    root = build_bst(items)

    assert root.item == 10
    assert root.left.item == 4
    assert root.right.item == 16
    assert root.left.right.item == 5
    assert root.right.right.item == 17
