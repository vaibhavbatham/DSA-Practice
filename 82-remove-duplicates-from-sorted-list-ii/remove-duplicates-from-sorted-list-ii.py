# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            store = curr.val
            if curr.next and curr.next.val == store:
                while curr and curr.val == store:
                    curr = curr.next

                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dummy.next