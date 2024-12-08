# T.C = O(N), travarsing all node once
# S.C = O(H), H is Max height of Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_symmetry(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False            

            return node1.val ==  node2.val and \
                    check_symmetry(node1.left, node2.right) and \
                    check_symmetry(node1.right, node2.left)
            
        return check_symmetry(root.left, root.right)