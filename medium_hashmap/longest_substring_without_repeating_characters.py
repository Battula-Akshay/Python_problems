class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_string = ""
        required_string_length = 0


        for i in range(len(s)):
            char_counts = {}
            
            for j in range(i,len(s)):
                current_string =  s[j]
                if current_string in char_counts:
                    # Duplicate found! Stop this row immediately
                    break
                else:
                    # Mark the character as seen
                    char_counts[current_string] = 1
                    
                # 3. Calculate current length using loop boundaries
                # (j - i + 1) gives the exact length of the current substring
                current_length = j - i + 1
                if required_string_length < current_length:
                    required_string_length = current_length




                   

                        

        return required_string_length
    
            
        
obj = Solution()
result = obj.lengthOfLongestSubstring("bbbbbb")
print(result)
