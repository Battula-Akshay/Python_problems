class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        final_list = []
        for i in nums1:
            

         # 1. Find exactly where 'i' lives in nums2
            start_index = nums2.index(i)
            
            # 2. Set a default answer of -1 (in case no greater number exists)
            ans = -1 
            
            
            for j in range(nums2.index(i) + 1,len(nums2)):
                    print("loop from","starting",nums2.index(i), "-->","ending",len(nums2))
                
                    if nums2[j] > i:
                        ans = nums2[j]
                        break
            final_list.append(ans)
        return final_list
obj = Solution()
result = obj.nextGreaterElement([4,1,2],[1,3,4,2])
print(result)

# test commit