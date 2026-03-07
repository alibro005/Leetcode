class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""

        for letter in s:
            if letter.isupper():
                letter = chr(ord(letter) + 32)
                result += letter

            else:
                result += letter
        return result
