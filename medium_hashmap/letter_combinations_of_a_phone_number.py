class Solution:

    def backtrack(self, current):
        print(len(current),"length")

        if len(current) == 3:
            print(current)
            return

        self.backtrack(current + "0")
        self.backtrack(current + "1")


obj = Solution()
obj.backtrack("")


        # map_letters_numbers = {
        #     "2" : "abc",
        #     "3" : "def",
        #     "4" : "ghi",
        #     "5" : "jkl",
        #     "6" : "mno",
        #     "7" : "pqrs",
        #     "8" : "tuv",
        #     "9" : "wxyz"
        # }
        # final_list = []

        # for i in map_letters_numbers[digits[0]]:
        #     for j in (map_letters_numbers[digits[1]]) :

                
        #         print(i,j)