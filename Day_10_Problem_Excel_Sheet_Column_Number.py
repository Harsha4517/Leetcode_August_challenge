class Solution:
    def titleToNumber(self, s: str) -> int:
        p=len(s)-1
        r=0
        for i in s:
            r+=(26**p)*(ord(i)-ord('A')+1)
            p-=1
        return r
