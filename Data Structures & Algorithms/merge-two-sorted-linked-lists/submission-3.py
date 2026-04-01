# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Took two hours to complete
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        i, j = (list1, list2) if list1.val < list2.val else (list2, list1)
        
        head = i
        while j != None:
            while i.next != None and j.val > i.next.val:
                i = i.next
            temp = i.next
            i.next = j
            j = temp
            i = i.next
        
        return head

