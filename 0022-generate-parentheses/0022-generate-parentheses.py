from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(current: str, open_left: int, close_left: int):

            if open_left == 0 and close_left == 0:
                result.append(current)

            if open_left > 0:
                helper(current + "(", open_left - 1, close_left)

            if close_left > open_left:
                helper(current + ")", open_left, close_left - 1)

        helper("", n, n)
        return result
