# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return
        if len(lists) == 1:
            return lists[0]
        
        head = temp = ListNode()

        while any(lists):
            mn = ListNode(val=5000)
            mni = -1
            # pick the least node
            for i in range(len(lists)):
                if lists[i] is None:
                    continue
                if lists[i].val < mn.val:
                    mn = lists[i]
                    mni = i
            if any(lists):
                head.next = mn
                lists[mni] = lists[mni].next
                head = mn
        return temp.next