class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num<=0:
            return False
        else:
            b=bin(num)
            r,z=0,0
            for i in b[::-1]:
                if i=='0' and z==0:
                    r+=1
                elif i=='1':
                    z+=1
                    if z>1:
                        return False
            if r%2==0:
                return True
            return False
