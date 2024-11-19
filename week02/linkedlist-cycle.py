# T.C = O(N)
# S.C = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        first, second = head, head

        while  second and second.next:
            first = first.next
            second = second.next.next
            if first == second :
                return True
        
        return False
        
