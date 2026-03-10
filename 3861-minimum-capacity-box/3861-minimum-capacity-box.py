class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        n = len(capacity)
        ans = -1
        for i in range(n):
            if capacity[i] >= itemSize:
                if ans == -1 or capacity[i] < capacity[ans]:
                    ans = i     
        return ans