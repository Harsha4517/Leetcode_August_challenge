class Solution:
    def toGoatLatin(self, S: str) -> str:
        r=''
        p='a'
        for i in S.split():
            if i[0] in ['a','e','i','o','u','A','E','I','O','U']:
                r+=i
                r+='ma'
                r+=p
            else:
                r+=i[1:]
                r+=i[0]
                r+='ma'
                r+=p
            r+=' '
            p+='a'
        return r[:len(r)-1]
