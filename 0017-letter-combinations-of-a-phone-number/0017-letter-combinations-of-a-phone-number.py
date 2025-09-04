class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = [""]

        for digit in digits:
            temp = []

            for comb in result:
                for char in phone_map[digit]:
                    temp.append(comb+char)
                result = temp
        return result
