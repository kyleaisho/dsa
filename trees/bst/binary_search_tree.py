from ..bst.node import Node


def build_bst(items) -> Node:
    if not items:
        return None
    root = Node(items.pop(0))

    for item in items:
        insert(root, item)
    return root


def insert(root: Node, item) -> Node:
    if not root:
        return Node(item)
    if item <= root.item:
        if not root.left:
            root.left = Node(item)
        else:
            insert(root.left, item)
    else:
        if not root.right:
            root.right = Node(item)
        else:
            insert(root.right, item)
    return root


def delete(node: Node, item) -> Node:
    pass
