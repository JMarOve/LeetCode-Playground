# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        res = dummy
        first = list1
        second = list2

        while first and second:
            if first.val < second.val:
                res.next=first
                first = first.next
            else:
                res.next=second
                second = second.next
            res=res.next
        if first:
            res.next = first
        elif second:
            res.next = second
       
        return dummy.next
        
