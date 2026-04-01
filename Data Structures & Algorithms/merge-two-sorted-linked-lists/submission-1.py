# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            i = list1
            j = list2
        else:
            i = list2
            j = list1
        
        head = i
        while j != None:
            while i.next != None and j.val > i.next.val:
                i = i.next
            temp = i.next
            i.next = j
            j = temp
            i = i.next
        
        return head

