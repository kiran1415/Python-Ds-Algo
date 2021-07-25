class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lst = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        my_set = set()
        for word in words:
            my_set.add(''.join(map(lambda x: lst[ord(x)-ord('a')],list(word))))
        return len(my_set)