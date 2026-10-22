# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:

        if head is None or head.next is None:
            return head

        length = 0
        last = head

        while last.next is not None:
            last = last.next
            length += 1

        length += 1

        k = k % length

        if k == 0:
            return head

        curr = head

        for i in range(length - k - 1):
            curr = curr.next

        last.next = head

        head = curr.next
        curr.next = None

        return head
