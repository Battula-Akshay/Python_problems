class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
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
        print(mapt)

        for i in mapt:
            if i in maps:

                if maps[i] != mapt[i]:
                    return i
            if i not in maps:
                return i
obj = Solution()
result = obj.findTheDifference("a","aa")
print(result)
