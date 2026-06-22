class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_map = {}
        stones_map = {}
        count = 0
        for i in jewels:
            if i in jewels_map:
                jewels_map[i] = jewels_map[i] + 1
            else:
                jewels_map[i] = 1

        for j in stones:
            if j in stones_map:
                stones_map[j] = stones_map[j] + 1
            else:
                stones_map[j] = 1

        for keys,values in jewels_map.items() :
            if keys in stones_map:
                count = count + stones_map[keys]
        return count
    
obj = Solution()
result = obj.numJewelsInStones("zz","aAAbbbb")
print(result)