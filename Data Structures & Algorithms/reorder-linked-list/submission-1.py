# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        # reverse LL from middle
        # calculate middle from counting length
        n = 0
        while head != None:
            n += 1
            head = head.next
        m = n // 2
        if n <= 2:
            return 
        # disconnect the LL from the middle
        middle = None
        i = 1
        head = temp
        while middle == None:
            if i == m:
                middle = head.next
                head.next = None
                break
            i += 1
            head = head.next

        # reverse linked list from middle
        prev = None
        while middle != None:
            temp2 = middle.next
            middle.next = prev
            prev = middle
            middle = temp2

        middle = prev
        head = temp

        # merge middle and head
        ans = ListNode()
        while head != None:
            t1 = head.next
            t2 = middle.next
            ans.next = head
            ans.next.next = middle
            ans = middle
            head = t1
            middle = t2   
        



        