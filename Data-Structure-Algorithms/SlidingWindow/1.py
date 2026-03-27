from collections import defaultdict
class Solution:
    def longestKSubstr(self, s, k):
        d = defaultdict(int)
        res = 0
        l,r = 0,0
        n = len(s)
        count = 0
        while r < n:
            while len(d) > k:
                d[s[l]] -=1
                count-=1
                if d[s[l]] == 0:
                    d.pop(s[l], None)
                l+=1
            d[s[r]] +=1
            if len(d) == k:
                count = r-l+1
                res = max(count, res)
            r+=1
        return res if res !=0 else -1
                
            
        
        