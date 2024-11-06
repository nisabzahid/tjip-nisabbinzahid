# T.C = O(N)
# S.C = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        carry = 0
        head = ListNode()
        node = head
        while first and second:
            total = carry + first.val + second.val
            curr = ListNode((total) % 10)
            carry = 1 if (total) > 9 else 0
            first = first.next
            second = second.next
            node.next = curr
            node = node.next
        
        while first :
            total = carry + first.val
            curr =  ListNode((total) % 10)
            carry = 1 if (total) > 9 else 0
            first = first.next
            node.next = curr
            node = node.next
        
        while second :

            total = carry + second.val
            curr =  ListNode((total) % 10)
            carry = 1 if (total) > 9 else 0
            second = second.next
            node.next = curr
            node = node.next

        if carry == 1:
            curr = ListNode(1)
            node.next = curr

        
        return head.next
