class Solution:
    def isAlpha(self,ch):
        if ('0' <= ch <= '9') or ('a' <= ch.lower() <= 'z'):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        result = ""
        for char in s:
            if self.isAlpha(char):
                result += char.lower()

        n = len(result)
        reverse = ""
        for char in result:
            reverse = char + reverse

        if reverse == result:
            return True

        return False
