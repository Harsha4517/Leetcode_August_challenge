class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        r=0
        //counting number of capital letters present
        for i in word:
            if i==i.upper():
                r+=1
        //checking the three conditions which satisfy the problem
        if r==0 or r==len(word) or (r==1 and word[0]==word[0].upper()):
            return True
        else:
            return False
