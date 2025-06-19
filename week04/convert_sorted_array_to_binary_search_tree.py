#T.C = O(N), creating all Treenode from array
#S.C = O(N)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create_tree(nums,start,end):
            if start > end:
                return None
            mid = (start+end)//2

            node = TreeNode(nums[mid])
            node.left = create_tree(nums,start, mid-1)
            node.right = create_tree(nums, mid+1, end)
            return node
        return create_tree(nums, 0 , len(nums)-1)