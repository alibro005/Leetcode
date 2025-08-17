class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
            result = []

            for num in range(left, right + 1):  
                n = num
                is_self_dividing = True

                while n > 0:
                    digit = n % 10
                    if digit == 0 or num % digit != 0:  
                        is_self_dividing = False
                        break
                    n //= 10

                if is_self_dividing:
                    result.append(num)

            return result


                