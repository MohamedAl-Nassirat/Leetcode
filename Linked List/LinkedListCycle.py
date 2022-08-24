# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # floyd's tortoise and hare algorithm
        # Fast pointer moves by 2, Slow pointer moves by 1
        # Time Complexity: O[n]
        fast, slow = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
                