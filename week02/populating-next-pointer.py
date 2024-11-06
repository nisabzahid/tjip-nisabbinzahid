# T.C = O(N)
# S.C = O(log(N))


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        node = root
        self.set_next(node)
        return root

    def set_next(self, node: 'optional[Node]') -> None:
        if not node or not node.left or not node.right:
            return
        node.left.next = node.right

        if node.next:
            node.right.next = node.next.left
        self.set_next(node.left)
        self.set_next(node.right)
        

