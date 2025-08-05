class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
    
        for i in range(0,n):
              result ^= start+2*i
          
        return result
    