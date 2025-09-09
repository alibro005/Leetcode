class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(','}':'{',']':'['}
        stack = []
    

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if (len(stack) == 0) or mapping[char] != stack.pop():
                    return False
        return len(stack) == 0


