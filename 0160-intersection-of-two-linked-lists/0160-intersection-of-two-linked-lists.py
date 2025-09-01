# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB

        l1 =  0
        l2 = 0

        while temp1 is not None:
            temp1 = temp1.next
            l1 += 1

        while temp2 is not None:
            temp2 = temp2.next
            l2 += 1

        slow = headA
        fast = headB

        if l1 > l2:
            for _ in range(l1 - l2):
                slow = slow.next
        else:
            for _ in range(l2 - l1):
                fast = fast.next

        while slow != fast:
                slow = slow.next
                fast = fast.next
            
        return slow