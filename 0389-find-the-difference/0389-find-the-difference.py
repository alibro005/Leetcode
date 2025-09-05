class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = {}
        s2 = {}

        for i in s:
            s1[i] = s1.get(i,0) + 1
        
        for i in t:
            s2[i] = s2.get(i,0) + 1

        
        for ch in s2:                    
            if ch not in s1 or s2[ch] != s1[ch]:
                return ch