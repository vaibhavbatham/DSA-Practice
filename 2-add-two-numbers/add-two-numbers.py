# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        curr1 = l1
        curr2 = l2

        ans = ListNode(-1)
        curr3 = ans
        rem = 0

        while curr1!= None or curr2!= None:
            total = rem
            rem = 0
            if curr1!= None:
                total += curr1.val
                curr1= curr1.next
            
            if curr2!= None:
                total += curr2.val
                curr2= curr2.next
            
            if total > 9 :
                rem = 1 # if we add single digit number max carry is 1
                total -= 10
            
            newNode = ListNode(total)
            curr3.next = newNode
            curr3 = curr3.next

        if rem > 0 :
            newNode = ListNode(rem)
            curr3.next = newNode
            curr3 = curr3.next

        return ans.next
                

        