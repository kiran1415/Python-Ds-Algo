class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")
        result = []            #To store the result
        
        for word in words:
            if set(word.lower()).issubset(first_row):        
                result.append(word)
            elif set(word.lower()).issubset(second_row):     
                result.append(word)
            elif set(word.lower()).issubset(third_row):      
                result.append(word)
        return result                                        
