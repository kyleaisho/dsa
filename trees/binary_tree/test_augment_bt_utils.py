from .augment_bt_utils import (
    build_bst,
    insert,
    delete,
    left_rotate,
    update_ancestors,
    right_rotate,
)


def test_build_augmented_tree():
    items = [10, 5, 15, 3, 7, 12, 19]
    root = build_bst(items)

    assert root.size == 7
    assert root.right.size == 3
    assert root.left.size == 3


def test_size_updates_after_insert():
    items = [10, 5, 15, 3, 7, 12, 19]
    root = build_bst(items)

    insert(root, 11)

    assert root.size == 8
    assert root.right.size == 4
    assert root.right.right.size == 1
    assert root.left.size == 3


def test_size_updates_after_insert():
    items = [10, 5, 15, 3, 7, 12, 19]
    root = build_bst(items)

    insert(root, 11)

    assert root.size == 8
    assert root.right.size == 4
    assert root.right.right.size == 1
    assert root.left.size == 3


def test_size_updates_after_delete():
    items = [10, 5, 15, 3, 7, 12, 19]
    root = build_bst(items)
    delete(root.right)

    assert root.size == 6


def test_height_updates_after_insert():
    items = [10, 5, 15, 3, 7, 12, 19]
    root = build_bst(items)

    assert root.height == 2
    assert root.right.height == 1
    assert root.right.right.height == 0
    assert root.left.height == 1

    insert(root, 11)

    assert root.height == 3
    assert root.right.height == 2
    assert root.left.height == 1


def test_size_updates_after_delete():
    items = [10, 5, 15, 3, 7, 12, 19]
    root = build_bst(items)
    delete(root.right)

    assert root.height == 2
    assert root.right.height == 1

    delete(root.right)
    delete(root.right)

    assert root.height == 2
    assert root.right == None
    assert root.left.height == 1


def test_left_rotate():
    items = [1, 2, 3, 4, 5]
    root = build_bst(items)

    assert root.height == 4

    root = left_rotate(root)
    assert root.item == 2
    assert root.left.item == 1
    assert root.height == 3


def test_manual_left_rotate_chain_to_balanced_tree():
    items = [1, 2, 3, 4, 5]
    root = build_bst(items)

    assert root.skew == 4
    left_rotate(root.right.right)
    left_rotate(root.right)
    left_rotate(root)
    left_rotate(root.left)

    assert root.item == 4
    assert root.right.item == 5
    assert root.left.item == 2
    assert root.left.left.item == 1
    assert root.left.right.item == 3

    assert root.height == 2
    assert root.skew == -1


def test_right_rotate():
    items = [5, 4, 3, 2, 1]
    root = build_bst(items)

    assert root.height == 4

    root = right_rotate(root)
    assert root.item == 4
    assert root.left.item == 3
    assert root.right.item == 5
    assert root.height == 3


def test_manual_right_rotate_chain_to_balanced_tree():
    items = [5, 4, 3, 2, 1]
    root = build_bst(items)

    assert root.skew == -4
    right_rotate(root.left.left)
    right_rotate(root.left)
    right_rotate(root)
    right_rotate(root.right)

    assert root.item == 2
    assert root.left.item == 1
    assert root.right.item == 4
    assert root.right.left.item == 3
    assert root.right.right.item == 5

    assert root.height == 2
    assert root.left.height == 0
    assert root.right.height == 1

    assert root.skew == 1
