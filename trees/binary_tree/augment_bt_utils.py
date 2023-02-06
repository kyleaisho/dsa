from typing import Optional
from .size_node import SizeNode as Node
from .binary_tree_utils import (
    insert as base_insert,
    node_factory,
    delete as base_delete,
    swap_nodes,
)


def build_bst(items) -> Node:
    if not items:
        return None
    root = Node(items.pop(0))

    for item in items:
        insert(root, item)
    return root


def update_ancestors(node: Node):
    if node:
        node.update()
        update_ancestors(node.parent)


def insert(node: Node, item) -> Node:
    inserted_node = base_insert(node, item, node_factory(Node))
    update_ancestors(inserted_node)
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
