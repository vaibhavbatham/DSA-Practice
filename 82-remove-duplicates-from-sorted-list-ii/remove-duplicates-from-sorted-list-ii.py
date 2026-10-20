# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        
        dummy = ListNode(0, head)
        sec = dummy
        curr = head

        while curr:
            store = curr.val

            if curr.next and curr.next.val == store:
                while curr and curr.val == store:
                    curr = curr.next

                sec.next = curr
            else:
                sec = curr
                curr = curr.next

        return dummy.next