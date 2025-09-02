# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = ListNode(0)
        prev.next = head
        temp = head
        head = prev

        while temp is not None:
            if temp.val == val:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return head.next