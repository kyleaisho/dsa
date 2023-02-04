from typing import Optional
from ..bst.node import Node


def build_bst(items) -> Node:
    if not items:
        return None
    root = Node(items.pop(0))

    for item in items:
        insert(root, item)
    return root


def insert(node: Node, item) -> Node:
    if not node:
        return Node(item)
    if item <= node.item:
        if not node.left:
            node.left = Node(item)
            node.left.parent = node
        else:
            insert(node.left, item)
    else:
        if not node.right:
            node.right = Node(item)
            node.right.parent = node
        else:
            insert(node.right, item)
    return node


def find(node: Node, item) -> Optional[Node]:
    if not node:
        return
    if node.item == item:
        return node
    return find(node.left, item) if item <= node.item else find(node.right, item)


def get_min(node: Node) -> Optional[Node]:
    if not node:
        return None
    if not node.left:
        return node
    return get_min(node.left)


def get_max(node: Node) -> Optional[Node]:
    if not node:
        return None
    if not node.right:
        return node
    return get_max(node.right)


def get_successor(node: Node) -> Optional[Node]:
    if not node:
        return
    if node.right:
        return get_min(node.right)
    # If there is no right subtree the successor is the
    # first left turn in my ancestor tree
    parent = node.parent
    current = node
    while parent and parent.right == current:
        current = parent
        parent = parent.parent

    return parent


def get_predecessor(node: Node) -> Optional[Node]:
    if not node:
        return None
    if node.left:
        return get_max(node.left)
    parent = node.parent
    while parent and parent.left == node:
        node = parent
        parent = parent.parent
    return parent


def is_leaf(node: Node) -> bool:
    return not (node.left or node.right)


def remove_from_parent(node: Node) -> bool:
    if node.parent.left == node:
        node.parent.left = None
    if node.parent.right == node:
        node.parent.right = None
    return True


def swap_nodes(n1: Node, n2: Node) -> None:
    tmp = n1.item
    n1.item = n2.item
    n2.item = tmp


def delete(node: Node) -> bool:
    if node is None:
        return False
    if is_leaf(node):
        return remove_from_parent(node)

    swap_node = get_predecessor(node) if node.left else get_successor(node)
    swap_nodes(node, swap_node)
    return delete(swap_node)
