class Solution:
    def power(self, x, n, mod):
        if n == 0:
            return 1

        half = self.power(x, n // 2, mod)
        result = (half * half) % mod

        if n % 2 == 1:
            result = (result * x) % mod

        return result

    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        even_count = (n + 1) // 2
        odd_count = n // 2

        return (self.power(5, even_count, MOD)) * (self.power(4, odd_count, MOD)) % MOD
