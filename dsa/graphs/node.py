class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.key = val
        self.adj = []

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __le__(self, other):
        return self.key <= other.key

    def __ge__(self, other):
        return self.key >= other.key
