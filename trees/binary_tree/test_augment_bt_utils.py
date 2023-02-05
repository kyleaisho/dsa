from .augment_bt_utils import build_bst, insert, delete


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
