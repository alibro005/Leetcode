class Solution:
    def reverse(self, s):
        return s[::-1]

    def reverseWords(self, s: str) -> str:
        words = s.split()

        result = []

        for word in words:
            result.append(self.reverse(word))

        return " ".join(result)
