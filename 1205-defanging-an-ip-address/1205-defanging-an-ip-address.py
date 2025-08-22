class Solution:
    def defangIPaddr(self, address: str) -> str:
        n = len(address)
        ans = ""

        for ch in range(n):
            if address[ch] != ".":
                ans += address[ch]
            else:
                ans += "[.]"

        return ans
