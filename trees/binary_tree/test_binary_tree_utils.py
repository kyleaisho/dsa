from .binary_tree_utils import (
    delete,
    get_max,
    get_predecessor,
    get_successor,
    insert,
    build_bst,
    find,
    get_min,
)


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


def test_find():
    items = [10, 4, 16, 5, 17, 21, 1]
    root = build_bst(items)

    assert find(root, 10) == root
    assert find(root, 4) == root.left
    assert find(root, 16) == root.right
    assert find(root, 5) == root.left.right


def test_get_min():
    items = [10, 4, 16, 5, 17, 21, 1]
    root = build_bst(items)

    assert get_min(root) == root.left.left
    assert get_min(root.right) == root.right
    assert get_min(root.left.left) == root.left.left
    assert get_min(root.right.right) == root.right.right


def test_get_max():
    items = [10, 4, 16, 5, 17, 21, 1]
    root = build_bst(items)

    assert get_max(root) == root.right.right.right
    assert get_max(root.left) == root.left.right
    assert get_max(root.left.left) == root.left.left


def test_get_successor():
    items = [10, 4, 17, 5, 16, 21, 1]
    root = build_bst(items)

    assert get_successor(None) == None
    assert get_successor(root) == get_min(root.right)
    assert get_successor(root.right.right) == None
    assert get_successor(root.left.left) == root.left


def test_get_predecessor():
    items = [10, 4, 17, 5, 16, 21, 1]
    root = build_bst(items)

    assert get_predecessor(None) == None
    assert get_predecessor(root) == get_max(root.left)
    assert get_predecessor(root.left) == root.left.left
    assert get_predecessor(root.right.right) == root.right


def test_delete():
    items = [10, 4, 17, 5, 16, 21, 1]
    root = build_bst(items)

    node = find(root, 1)
    delete(node)
    assert root.left.left is None
    insert(root, 1)

    node = find(root, 4)
    assert delete(node)
    assert root.left.item == 1
    assert root.left.left is None
    assert root.left.right.item == 5

    node = find(root, 10)
    delete(node)
    assert root.item == 5
    assert find(root, 10) is None

    node = find(root, 17)
    delete(node)
    assert root.right.item == 16
    assert find(root, 17) == None

    insert(root, 19)
    assert root.right.right.left.item == 19

    node = find(root, 21)
    delete(node)
    assert root.right.right.item == 19
    assert root.right.right.right is None
    assert root.right.right.left is None
