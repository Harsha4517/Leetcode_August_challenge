class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        x=0
        for i in d:
            if d[i]&1:
                x+=d[i]-1
            else:
                x+=d[i]
        if x<len(s):
            return x+1
        return x
