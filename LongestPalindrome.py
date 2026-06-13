class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        has_odd = False
   
        maps = {}
        for i in s:
            if i not in maps :
                maps[i] = 1
            else:
                maps[i] = maps[i] + 1
        print(maps)

        for i in maps:
            if len(maps) == 1:
                return len(s)
            if maps[i] % 2 == 0:
                count = count + maps[i]
            if maps[i] %2 != 0:
                has_odd = True
                count = count + maps[i] - 1
        if has_odd == True:
            return count + 1

     




           
        return count
obj = Solution()
result = obj.longestPalindrome("abbccccdd")
print(result)