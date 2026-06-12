class Solution:
    def firstUniqChar(self, s: str) -> int:
        maps = {}
        for i in s:
            if i in maps:
                maps[i] = maps[i] + 1
            else:
                maps[i] = 1
        print(maps)

        for index,char in enumerate(s):
          

            if maps[char] == 1:
                
                    return index
                
        return -1
obj = Solution()
result = obj.firstUniqChar("dddccdbba")
print(result)