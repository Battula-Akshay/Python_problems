class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:

        first_idx = {}
        last_idx = {}
        counts = {}
        
        # Track first index, last index, and count for each number
        for i, num in enumerate(nums):
            if num not in first_idx:
                first_idx[num] = i
            last_idx[num] = i
            counts[num] = counts.get(num, 0) + 1
            
        # Find the degree (maximum frequency) of the array
        degree = max(counts.values())
        
        # Find the minimum length among all elements that match the degree
        min_len = len(nums)
        for num in counts:
            if counts[num] == degree:
                length = last_idx[num] - first_idx[num] + 1
                if length < min_len:
                    min_len = length
                    
        return min_len

                
 
                

    

obj = Solution()
result = obj.findShortestSubArray([1,1])
print(result)