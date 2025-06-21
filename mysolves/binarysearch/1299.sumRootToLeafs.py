# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = []

        def dfs(node, s):
            print(node.val, s)
            s+= str(node.val)
            if not node.left and not node.right:
                paths.append(int(s))
                return
            if node.left:
                dfs(node.left, s )
            if node.right:
                dfs(node.right, s)

        dfs(root, "")
        print(paths)
        return sum(paths)