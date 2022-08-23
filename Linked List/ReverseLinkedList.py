# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # First we want to set the previous node to None, and current node to the head node
        # Transverse through the Linked List and assign a temp variable to hold the next node
        # Set the next node to be the previous pointer and current pointer to be to the temp node 
        
        
        previous = None
        current = head
        
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous