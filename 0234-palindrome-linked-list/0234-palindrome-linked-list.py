# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head: ListNode) -> ListNode:
        temp = head
        prev = None

        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        rev = self.reverse(slow)
        temp = head

        while rev is not None:
            if temp.val != rev.val:
                return False
            temp = temp.next
            rev = rev.next

        return True
