class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 :
            if n is seen:
                return False
            seen.add(n)
            total = 0
            for digit in str(n):
                total = total + int(digit)**2
            n = total
        return True
 

                


                
        
                    
obj = Solution()
result = obj.isHappy(2)
print(result)