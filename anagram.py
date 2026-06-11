class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = {}
        mapt = {}
        for i in s:
            if i in maps:
                maps[i] = maps[i] + 1
            else:
                maps[i] = 1
                
        print(maps)
        for i in t:
            if i in mapt:
                mapt[i] = mapt[i] + 1
            else:
                mapt[i] = 1
                
        print(maps,mapt)
        return maps == mapt

obj = Solution()
result = obj.isAnagram("anagram","agaram")
print(result)