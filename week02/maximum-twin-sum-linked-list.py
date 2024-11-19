# T.C = O(N)
# S.C = O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = self.get_length(head)
        second_half_head , first_half_reversed = self.reverse_first_half(head, length)
        max_twin_sum = 0
        
        for _ in range(length//2) :
            max_twin_sum = max(max_twin_sum, second_half_head.val + first_half_reversed.val)
            second_half_head = second_half_head.next
            first_half_reversed = first_half_reversed.next
        return max_twin_sum

    def reverse_first_half(self, node, length):
            current = node
            reversed_list = None

            for _ in range(length //2):
                next_node = current.next
                current.next = reversed_list
                reversed_list = current
                current = next_node
            return current, reversed_list
        
    def get_length(self, head):
        length = 0
        current = head
        while current:
            length +=1
            current = current.next
        return length