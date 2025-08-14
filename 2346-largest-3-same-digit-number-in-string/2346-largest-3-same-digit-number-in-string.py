class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = ""
        for i in range(2, len(num)):
            if num[i] == num[i - 1] == num[i - 2]:
                triplet = num[i - 2 : i + 1]
                if triplet > largest:
                    largest = triplet
        return largest
