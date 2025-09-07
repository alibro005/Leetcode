class Solution:
    def next_digit(self,n:int) -> int:
        total = 0

        while n != 0:
            last_digit = n % 10
            total += last_digit * last_digit
            n //= 10
        return total

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.next_digit(n)

        while fast != 1 and slow != fast:
            slow = self.next_digit(slow)
            fast = self.next_digit(self.next_digit(fast))
        
        return fast == 1
        