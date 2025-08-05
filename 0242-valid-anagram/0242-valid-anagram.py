class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            letter1 = dict()
            letter2 = dict()

            for i in range(len(s)):
                letter1[s[i]]= letter1.get(s[i],0) + 1
                letter2[t[i]] = letter2.get(t[i],0) + 1
            
            if letter1 == letter2:
                return True
            else:
                return False


