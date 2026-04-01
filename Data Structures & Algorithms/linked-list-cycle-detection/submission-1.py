# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # no duplicates?
        if head is None:
            return False
        hashset = set()
        while head.next != None:
            if head.val in hashset:
                return True
            else:
                hashset.add(head.val)
            head = head.next
        return False
        