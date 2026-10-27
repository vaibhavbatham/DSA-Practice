# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # Pointers to traverse both input linked lists
        curr1 = l1
        curr2 = l2

        # Dummy node to simplify creating the result linked list
        dummy = ListNode(-1)
        curr3 = dummy

        # Carry generated during addition
        carry = 0

        # Continue while either list has nodes remaining
        while curr1 is not None or curr2 is not None:

            # Start with the carry from the previous addition
            total = carry
            carry = 0

            # Add the digit from the first list, if available
            if curr1 is not None:
                total += curr1.val
                curr1 = curr1.next

            # Add the digit from the second list, if available
            if curr2 is not None:
                total += curr2.val
                curr2 = curr2.next

            # If the sum is 10 or greater, generate a carry
            if total > 9:
                carry = 1
                total -= 10

            # Create a new node containing the result digit
            new_node = ListNode(total)

            # Attach the new node to the result linked list
            curr3.next = new_node
            curr3 = curr3.next

        # If a carry remains, add it as the final node
        if carry > 0:
            new_node = ListNode(carry)
            curr3.next = new_node

        # Return the head of the result list, skipping the dummy node
        return dummy.next


        