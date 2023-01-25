
from typing import List


def build_binary_tree(nums: List[int]):
    root = BinaryTreeNode(nums.pop(0))

    for val in nums:
        root.insert(val)
    
    return root


def height(A):
    if A is None:
        return -1
    return A.height

class BinaryTreeNode:
    def __init__(A, value) -> None:
        A.item = value
        A.left = None
        A.right = None
        A.parent = None
        A.subtree_update()
    
    def subtree_update(A):
        A.height = 1 + max(height(A.left), height(A.right))

    def insert(A, value):
        if value <= A.item:
            if A.left is None:
                A.left = BinaryTreeNode(value)
            else:
                A.left.insert(value)
            A.left.parent = A
        else:
            if A.right is None:
                A.right = BinaryTreeNode(value)
            else:
                A.right.insert(value)
            A.right.parent = A
        A.subtree_update()


    def find(A, value):
        if A is None or A.item == value:
            return A
        if value <= A.item:
            return A.left.find(value)
        else:
            return A.right.find(value)        

    def find_next(A, value):
        pass

    def find_prev(A, value):
        pass

    def get_min(A):
        return A if A.left is None else A.left.get_min()

    def get_max(A):
        return A if A.right is None else A.right.get_max()
        

    def successor(A):
        """Successor is defined as the smallest key that is still greater than the current key"""
        if A.right:
            return A.right.get_min()
        
        # walk up the ancestors until there is a right subtree
        # then return to the parent node of the right subtree's root
        parent = A.parent
        current = A
        while parent and parent.right == current:
            current = parent
            parent = parent.parent
        
        return parent
        

    def predecessor(A, value):
        pass
