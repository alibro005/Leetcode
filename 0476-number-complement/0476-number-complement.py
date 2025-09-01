class Solution:
    def findComplement(self, num: int) -> int:

        
        result = ""
        while num > 0:
            if num % 2 == 1:
                result += "1"
            else:
                result += "0"
            num //= 2
        result = result[::-1]
        
        flip = ""
        for i in result:
            if i == "1":
                flip += "0"
            else:
                flip += "1"

        decimal_no = 0
        power = 0
        index = len(flip) - 1

        while index >= 0:
            num = int(flip[index]) * (2**power)
            decimal_no += num
            index -= 1
            power += 1

        return decimal_no