from typing import Optional, Union
from .size_node import SizeNode as Node
from .binary_tree_utils import (
    insert as base_insert,
    node_factory,
    delete as base_delete,
    swap_nodes,
)


def build_bst(items, NodeClass=Node):
    if not items:
        return None
    root = NodeClass(items.pop(0))

    for item in items:
        insert(root, item, NodeClass)
    return root


def update_ancestors(node):
    if node:
        node.update()
        update_ancestors(node.parent)


def insert(node, item, NodeClass=Node):
    inserted_node = base_insert(node, item, NodeClass)
    inserted_node.update()
    return inserted_node


def delete(node: Node) -> bool:
    return base_delete(node, update_ancestors)


def left_rotate(node: Node) -> Optional[Node]:
    if not node or not node.right:
        return None

    A = node.left
    B = node.right.left
    C = node.right.right

    # Change the values of node and its right child
    swap_nodes(node, node.right)

    # Rebuild the tree starting from node
    node.left = node.right
    node.left.left = A
    node.left.right = B
    node.right = C

    update_ancestors(node.left)

    return node


def right_rotate(node: Node) -> Optional[Node]:
    if not node or not node.left:
        return None

    A = node.left.left
    B = node.left.right
    C = node.right

    # Change the values of node and its right child
    swap_nodes(node, node.left)

    # Rebuild the tree starting from node
    node.right = node.left
    node.left = A
    node.right.left = B
    node.right.right = C

    update_ancestors(node.right)

    return node


def rotate_if_needed(node: Node):
    if node.skew == 2:
        if node.right.skew == -1:
            right_rotate(node.right)
        left_rotate(node)
    if node.skew == -2:
        if node.left.skew == 1:
            left_rotate(node.left)
        right_rotate(node)
