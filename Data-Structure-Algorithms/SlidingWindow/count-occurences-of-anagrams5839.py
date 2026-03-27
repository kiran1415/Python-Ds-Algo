"""
Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.

Example 1:

Input: txt = "forxxorfxdofr", pat = "for"
Output: 3
Explanation: for, orf and ofr appears in the txt, hence answer is 3.
Example 2:

Input: txt = "aabaabaa", pat = "aaba"
Output: 4
Explanation: aaba is present 4 times in txt.
Constraints:
1 <= |pat| <= |txt| <= 105
Both strings contain lowercase English letters.

"""


from collections import defaultdict
class Solution:

	
	def search(self,pat, txt):
	    d1 = defaultdict(int)
	    d2 = defaultdict(int)
	    
	    count = 0
	    
	    k = len(pat)
	    
	    for char in pat:
	        d1[char]+=1
	    
	    i,j = 0,0
	    
	    while j-i+1 <= k:
	        d2[txt[j]] +=1
	        j+=1
	    
	    if d2 == d1:
	        count+=1
	    
	    while j < len(txt):
	        d2[txt[j]] +=1
	        d2[txt[i]] -=1
	        if d2[txt[i]] == 0:
	            del d2[txt[i]]
	        if d2 == d1:
	            count+=1
	        i+=1
	        j+=1
	    return count
	        
	        
	    
	    
