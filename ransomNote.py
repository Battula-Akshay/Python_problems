class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapr = {}
        mapm = {}
        for i in ransomNote:
            if i in mapr:
                mapr[i] = mapr[i] + 1
            else:
               mapr[i] = 1 
        print(mapr)
        for i in magazine:
            if i in mapm:
                mapm[i] = mapm[i] + 1
            else:
               mapm[i] = 1 
        print(mapm)
        for i in mapr:
            if i not in mapm:
                return False
            if i in mapm:
                if mapr[i] > mapm[i]:
                    return False

        return True
                
         
obj = Solution()
result = obj.canConstruct("bg","efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")
print(result)
        
        