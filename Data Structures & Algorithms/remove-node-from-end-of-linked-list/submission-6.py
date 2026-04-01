# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = head
        slow = None
        prev_slow = None
        i = 0
        while fast:
            i += 1
            # activate slow pointer
            if slow:
                prev_slow = slow
                slow = slow.next
            if abs(i-n) == 0:
                slow = head
            fast = fast.next
        if slow is None:
            return None
        if prev_slow is None:
            head = slow.next
        else:
            prev_slow.next = slow.next
        return head


            
        