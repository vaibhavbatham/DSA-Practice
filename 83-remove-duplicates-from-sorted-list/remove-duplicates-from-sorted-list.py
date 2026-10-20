# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        
        if head is None:
            return head 
            
        first = head
        sec =  head.next

        while sec != None:
            
            if first.val == sec.val:
                first.next = sec.next
                sec = sec.next
            else:
                sec = sec.next
                first = first.next

        return head

            
