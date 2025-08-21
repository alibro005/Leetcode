class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        n = len(s)
        length = 0
        i = n - 1

        for i in range(n-1, -1,-1):
            if s[i] == " ":
                break
            length += 1
        return length
        
            
                