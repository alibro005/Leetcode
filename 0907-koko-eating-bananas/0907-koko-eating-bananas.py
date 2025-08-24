class Solution:
    def speed(self,piles,speed,h):
        hrs = 0
        for pile in piles:
            hrs += (pile + speed - 1) // speed
        
        return hrs <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        start , end = 1 , max(piles)
        ans = end

        while start <= end:
            mid = start + (end - start)//2

            if self.speed(piles,mid,h):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return ans

            