class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        map_licensePlate = {}
        map_words = {}
        similar_words = []
        similar_licenseplate_words = []
        cleaned_word = ""
        final_word_list = {}
    #this for loop is for extracting only words of license plate and converting them to lower
        for char in licensePlate:
            if char.isalpha():           
                cleaned_word = char.lower() + cleaned_word 
        # print(cleaned_word)    
            
    # this loop is for converting license plate to map to see how many times it is repeating
        for i in cleaned_word:
            if i in map_licensePlate:
                map_licensePlate[i] = map_licensePlate[i] + 1
            else:
                map_licensePlate[i] = 1 
        # print(map_licensePlate)
    # now we take each word from words and compare it with the license plate 
    #we are adding these words to map_words 
    # I want to add each word to map_words and compare it with map_license plate 
        for i in range(len(words)):
            current_word = words[i]
            similar_licenseplate_words = []   
            map_words = {}
            #I am converting each word to map -->map_words
            for j in words[i]:

                if j.lower() in map_words:
                    map_words[j.lower()] = map_words[j.lower()] + 1
                else:
                    map_words[j.lower()] = 1 

            print(map_words,":","map_words")
            print(cleaned_word,":","cleaned word")
            print(map_licensePlate,":","License plate map")
            #now comparing each word with the map_license_plate
            for k in map_licensePlate:
            
                if k  in map_words:
                    if map_licensePlate[k] >= map_words[k] :
                        similar_licenseplate_words.append(k)
            
            print(map_words)
            print(similar_licenseplate_words)
            if len(similar_licenseplate_words) == len(map_licensePlate):
                     current_word = words[i]
                     similar_words.append(current_word)
        for h in similar_words:
            m = 0
            if h in final_word_list :
                final_word_list[h] = final_word_list[h] + 1
            else:
                final_word_list[h] = m + 1
                m = m + 1


        print(final_word_list)

                     
                
        return current_word,similar_words
            
obj = Solution()
result = obj.shortestCompletingWord("1s3 456",["looks","pest","stew","show"])
print(result)

