class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        n = len(operations)
        prefix = 0
        for op in operations:
            if op == "X++" or op == "++X":
               prefix += 1
            else:
               prefix -= 1

    
        return prefix
