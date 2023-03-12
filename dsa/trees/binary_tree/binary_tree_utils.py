from typing import Optional, Union
from .node import Node
from .size_node import SizeNode

NodeType = Union[Node, SizeNode]


def build_bst(items) -> NodeType:
    if not items:
        return None
    root = Node(items.pop(0))

    for item in items:
        insert(root, item)
    return root


def node_factory(NodeConstructor=Node) -> callable:
    def construct(*args, **kwargs):
        return NodeConstructor(*args, **kwargs)

    return construct


def insert(node: NodeType, item, construct_node=node_factory()) -> NodeType:
    if not node:
        return construct_node(item)
    if item <= node.item:
        if not node.left:
            node.left = construct_node(item)
            node.left.parent = node
        else:
            return insert(node.left, item, construct_node)
    else:
        if not node.right:
            node.right = construct_node(item)
            node.right.parent = node
        else:
            return insert(node.right, item, construct_node)
    return node


def find(node: NodeType, item) -> Optional[NodeType]:
    if not node:
        return
    if node.item == item:
        return node
    return find(node.left, item) if item <= node.item else find(node.right, item)


def get_min(node: NodeType) -> Optional[NodeType]:
    if not node:
        return None
    if not node.left:
        return node
    return get_min(node.left)


def get_max(node: NodeType) -> Optional[NodeType]:
    if not node:
        return None
    if not node.right:
        return node
    return get_max(node.right)


def get_successor(node: NodeType) -> Optional[NodeType]:
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


def get_predecessor(node: NodeType) -> Optional[NodeType]:
    if not node:
        return None
    if node.left:
        return get_max(node.left)
    parent = node.parent
    while parent and parent.left == node:
        node = parent
        parent = parent.parent
    return parent


def is_leaf(node: NodeType) -> bool:
    return not (node.left or node.right)


def remove_from_parent(node: NodeType, augment_update=None) -> bool:
    if node.parent.left == node:
        node.parent.left = None
    if node.parent.right == node:
        node.parent.right = None

    if augment_update:
        augment_update(node)

    return True


def swap_nodes(n1: NodeType, n2: NodeType) -> None:
    tmp = n1.item
    n1.item = n2.item
    n2.item = tmp


def delete(node: NodeType, augment_update=None) -> bool:
    if node is None:
        return False
    if is_leaf(node):
        return remove_from_parent(node, augment_update)

    swap_node = get_predecessor(node) if node.left else get_successor(node)
    swap_nodes(node, swap_node)
    return delete(swap_node, augment_update)
