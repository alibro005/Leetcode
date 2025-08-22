class Solution:
    def squareOfdigits(self, n):
        result = 0
        while n != 0:
            digit = n % 10
            result += digit**2
            n //= 10
        return result

    def isHappy(self, n: int) -> bool:

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.squareOfdigits(n)

        return n == 1
