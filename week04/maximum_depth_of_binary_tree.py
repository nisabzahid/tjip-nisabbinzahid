#T.C = O(N)
#S.C = O(1)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def find_max_depth(node, curr_depth):
            if not node:
                return curr_depth - 1  # Return depth when reaching a null node
            left_depth = find_max_depth(node.left, curr_depth + 1)
            right_depth = find_max_depth(node.right, curr_depth + 1)
            return max(left_depth, right_depth)
        
        return find_max_depth(root, 1)
