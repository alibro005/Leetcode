# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next
        
        if fast == None:
            return head.next
        
        while fast.next is not None:

            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head



















        # length = 0
        # temp = head 

        # while temp is not None:
        #     length += 1
        #     temp = temp.next
        
        # if length == n:
        #     new_head = head.next
        #     return new_head
        
        # position_stop = length - n

        # temp = head
        # count = 1
        # while count < position_stop:
        #     temp = temp.next
        #     count += 1
        # temp.next = temp.next.next

        # return head
