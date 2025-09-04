class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        phone_map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        result = []

        def helper(index:int,current:str):

            if index == len(digits):
                result.append(current)
                return
            
            for char in phone_map[digits[index]]:
                helper(index+1,current+char)
        
        helper(0,"")
        return result