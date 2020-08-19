class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l=[1]
        for i in range(1,rowIndex+1):
            l.append((l[i-1]*(rowIndex-i+1))//i)
        return l
