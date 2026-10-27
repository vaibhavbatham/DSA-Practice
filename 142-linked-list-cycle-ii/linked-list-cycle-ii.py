# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Step 1: Detect the cycle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Step 2: Calculate cycle length
        lengthCountOfLoop = 1
        curr = slow.next

        while curr != slow:
            curr = curr.next
            lengthCountOfLoop += 1

        # Step 3: Move fast ahead by cycle length
        slow = head
        fast = head

        for i in range(lengthCountOfLoop):
            fast = fast.next

        # Step 4: Find the cycle's starting node
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

