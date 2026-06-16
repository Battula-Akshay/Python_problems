class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        max_element = 0
        loop_count = 0
        most_frequent_key = None
        maps = {}
        list_range = [] 
        for i in (nums):
            if i in maps:
               maps[i] = maps[i] + 1
            else:
                maps[i] = 1 
        for i in maps:
                
            if maps[i] > max_element:
              max_element = maps[i]
              most_frequent_key = i
        print("most_frequent_key",":",most_frequent_key,"maps",":",maps)
        for i in range(len(nums)):
            if nums[i] == 2:
                list_range.append(i)
        print("most repeated values are present in this range",":",list_range)
        # print("index 0 value ",":",list_range[0],"index last value",":",list_range[len(list_range)-1])
        print("list_range",":",list_range)
        if len(nums) == 1:
            return 1
        else:
            for i in range(list_range[0],max(list_range) + 1):
                print("for loop is running from",":",list_range[0],"-->",max(list_range))
                if (max(list_range) ) - list_range[0] == 1:
                    return 2
                else:
                    loop_count = loop_count + 1
            return loop_count
                
 
                

    

obj = Solution()
result = obj.findShortestSubArray([1,1])
print(result)