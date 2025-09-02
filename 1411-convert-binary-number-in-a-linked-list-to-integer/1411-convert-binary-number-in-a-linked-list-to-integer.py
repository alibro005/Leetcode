# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # result = ""
        # temp = head

        # while temp is not None:
        #     s = str(temp.val)
        #     result += s
        #     temp = temp.next

        # decimal_no = 0
        # power = 0
        # index = len(result) - 1

        # while index >= 0:
        #     num = int(result[index]) * (2**power)
        #     decimal_no += num
        #     index -= 1
        #     power += 1

        # return decimal_no

        result = 0
        temp = head

        while temp:
            result = result * 2 + temp.val
            temp = temp.next

        return result
