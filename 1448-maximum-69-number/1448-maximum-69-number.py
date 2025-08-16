class Solution:
    def maximum69Number(self, num: int) -> int:
        n = num
        pos = -1
        i = 0

        while n > 0:
            digit = n % 10
            if digit == 6:
                pos = i
            n //= 10
            i += 1

        if pos == -1:
            return num

        result = num + 3 * (10**pos)

        return result
