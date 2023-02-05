from .size_node import SizeNode as Node
from .binary_tree_utils import (
    insert as base_insert,
    node_factory,
    delete as base_delete,
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
