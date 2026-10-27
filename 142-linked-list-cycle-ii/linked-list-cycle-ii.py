# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize slow and fast pointers
        slow = head
        fast = head

        # Step 1: Detect whether a cycle exists
        while fast is not None and fast.next is not None:
            slow = slow.next          # Move one step
            fast = fast.next.next     # Move two steps

            # If both pointers meet, a cycle exists
            if slow == fast:

                # Step 2: Find the starting node of the cycle
                temp = head

                while temp != slow:
                    temp = temp.next
                    slow = slow.next

                # The meeting point is the cycle's starting node
                return temp

        # If fast reaches the end, there is no cycle
        return None