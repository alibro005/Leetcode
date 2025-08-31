# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq_map = {}
        temp = head

        while temp is not None:
            freq_map[temp.val] = freq_map.get(temp.val, 0) + 1
            temp = temp.next

        dummy = ListNode(0)
        curr = dummy
        temp = head
        while temp is not None:
            if freq_map[temp.val] == 1:   
                curr.next = ListNode(temp.val)
                curr = curr.next
            temp = temp.next

        return dummy.next