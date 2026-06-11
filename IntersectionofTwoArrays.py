class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        map_nums1 = {}
        map_nums2 = {}
        list1 = []

        for i in nums1:
            if i in map_nums1:
                map_nums1[i] = map_nums1[i] + 1
            else:
                map_nums1[i] = 1
        for i in nums2:
            if i in map_nums2:
                map_nums2[i] = map_nums2[i] + 1
            else:
                map_nums2[i] = 1
        for i in map_nums1:
            if i in map_nums2:
             res = list1.append(i)
        return(list1)
        

obj = Solution()
result = obj.intersection([4,9,5],[9,4,9,8,4])
print(result)