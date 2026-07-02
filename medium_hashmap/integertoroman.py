class Solution:
    def intToRoman(self, num: int) -> str:
        map_roman = {
            1000 : "M",
            900  : "CM",  
            500  : "D",
            400  : "CD",
            100  : "C",
            90   : "XC",
            50   : "L",
            40   : "XL",
            10   : "X",
            9    : "IX",
            5    : "V",
            4    : "IV",
            1    : "I",
        }
        result = ""
        for key,value in map_roman.items():
            if num >= key:
                # result = result + value
                rem = num // key
                if rem > 1:
                    result = result + rem*value
                else:
                    result = result + value
                num = num - rem*key
               
                

        return(result)
 

        
obj = Solution()
result = obj.intToRoman(3749)
print(result)