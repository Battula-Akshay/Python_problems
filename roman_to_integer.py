class Solution:

    # print(hash_map)
    sum1 = 0

    
    def romanToInt(self, s: str) -> int:
        hash_map = {}
        hash_map["I"] = 1
        hash_map["V"] = 5
        hash_map["X"] = 10
        hash_map["L"] = 50
        hash_map["C"] = 100
        hash_map["D"] = 500
        hash_map["M"] = 1000

        l = 0
        z = 1
        first_number = 0
        total_sum = 0

        while z < len(s):
            k = hash_map[s[l]]
            m = hash_map[s[z]]

       
            if k >= m:
                total_sum = k + total_sum
                l = l + 1
                z = z + 1
            else :
                subtraction = m - k
                total_sum = subtraction + total_sum
                l = l + 2
                z = z + 2
        if l < len(s):
            total_sum += hash_map[s[l]]

        return(total_sum)


romantoInt = Solution()
result = romantoInt.romanToInt("IV")
print(result)