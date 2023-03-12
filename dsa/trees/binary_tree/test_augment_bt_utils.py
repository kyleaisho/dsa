from unittest.mock import Mock
from unittest.mock import patch
from .augment_bt_utils import (
    build_bst,
    insert,
    delete,
    left_rotate,
    right_rotate,
    rotate_if_needed,
)
from .size_node import SizeNode
from .avl_node import AVLNode


def test_build_augmented_tree():
    items = [10, 5, 15, 3, 7, 12, 19]
    root = build_bst(items, SizeNode)

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


@patch("trees.binary_tree.augment_bt_utils.right_rotate")
@patch("trees.binary_tree.augment_bt_utils.left_rotate")
def test_rotate_if_needed_balanced(mock_right: Mock, mock_left: Mock):
    balanced = build_bst([10, 5, 15, 2, 12, 17, 7])

    rotate_if_needed(balanced.right.right)
    rotate_if_needed(balanced.right.left)
    rotate_if_needed(balanced.left.right)
    rotate_if_needed(balanced.left.left)

    mock_right.assert_not_called()
    mock_left.assert_not_called()


@patch("trees.binary_tree.augment_bt_utils.right_rotate")
@patch("trees.binary_tree.augment_bt_utils.left_rotate")
def test_rotate_if_needed_small_skew_left(mock_right: Mock, mock_left: Mock):
    balanced = build_bst([15, 5, 10, 2, 12, 17, 7])

    rotate_if_needed(balanced.right)
    rotate_if_needed(balanced.left.left)
    rotate_if_needed(balanced.left.right.right)

    mock_right.assert_not_called()
    mock_left.assert_not_called()


@patch("trees.binary_tree.augment_bt_utils.right_rotate")
@patch("trees.binary_tree.augment_bt_utils.left_rotate")
def test_rotate_if_needed_small_skew_right(mock_right: Mock, mock_left: Mock):
    balanced = build_bst([5, 10, 15, 2, 12, 17, 7])

    rotate_if_needed(balanced.right.right.right)
    rotate_if_needed(balanced.right.left)
    rotate_if_needed(balanced.left)

    mock_right.assert_not_called()
    mock_left.assert_not_called()


def test_rotate_needed_case_right_skew_negative():
    root = build_bst([1, 2, 3])

    rotate_if_needed(root)
    assert root.item == 2
    assert root.left.item == 1
    assert root.right.item == 3


def test_rotate_needed_case_right_skew_negative():
    root = build_bst([10, 15, 13])

    assert root.skew == 2
    assert root.right.skew == -1

    rotate_if_needed(root)
    assert root.skew == 0
    assert root.item == 13
    assert root.left.item == 10
    assert root.right.item == 15


def test_rotate_if_needed_case_left_skew_positive():
    root = build_bst([10, 5, 7])

    assert root.skew == -2
    assert root.left.skew == 1

    rotate_if_needed(root)

    assert root.skew == 0
    assert root.item == 7
    assert root.left.item == 5
    assert root.right.item == 10


def test_rotate_if_needed_case_left_skew_negative():
    root = build_bst([10, 5, 3])

    assert root.skew == -2
    assert root.left.skew == -1

    rotate_if_needed(root)

    assert root.skew == 0
    assert root.item == 5
    assert root.left.item == 3
    assert root.right.item == 10


def test_rotate_if_needed_parent_still_points_to_subtree():
    root = build_bst([20, 10, 5, 7])
    left = root.left
    rotate_if_needed(root.left)
    root.left == left


def test_create_avl_tree():
    root_bt = build_bst([1, 2, 4, 5, 6])
    root_avl = build_bst([1, 2, 4, 5, 6], AVLNode)

    assert root_bt.skew == 4
    assert root_avl.skew == 0
