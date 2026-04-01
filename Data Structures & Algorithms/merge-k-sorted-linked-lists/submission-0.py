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
        
        head = last = ListNode(val=-5000)

        while any(lists):
            for i in range(len(lists)):
                if lists[i] is None:
                    break
                # insert at last
                if lists[i].val >= last.val:
                    last.next = lists[i]
                    last = last.next
                    lists[i] = lists[i].next
                # if smaller than head
                elif lists[i].val <= head.val:
                    temp = head
                    head = lists[i]
                    head.next = temp
                    lists[i] = lists[i].next
                else:
                    curr = head
                    # if not, need to find the insert position
                    while curr.next.val < lists[i].val:
                        curr = curr.next

                    t1 = lists[i].next
                    t = curr.next
                    curr.next = lists[i]
                    curr.next.next = t
                    lists[i] = t1
        return head.next
                    
                        

        