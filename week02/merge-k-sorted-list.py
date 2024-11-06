# T.C = O(N*log(k))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        min_heap = []
        for index in range(len(lists)): # O(N*log(K))
            if lists[index]:
                heapq.heappush(min_heap,(lists[index].val, index, lists[index] ))


        dummy_head = ListNode(0)
        current = dummy_head
        while min_heap: # O(N*log(K))
            _, index , node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val,index, node.next))
        
        return dummy_head.next



