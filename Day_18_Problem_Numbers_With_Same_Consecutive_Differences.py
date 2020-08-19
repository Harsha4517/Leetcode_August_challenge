class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        l=[1,2,3,4,5,6,7,8,9]
        if N==1:
            return [0,1,2,3,4,5,6,7,8,9]
        for i in range(2,N+1):
            p=[]
            for j in l:
                z=j%10
                if z-K==z+K:
                    p.append(j*10+z+K)
                    continue
                if z-K>=0:
                    p.append(j*10+z-K)
                if z+K<=9:
                    p.append(j*10+z+K)
            l=p
        return l
