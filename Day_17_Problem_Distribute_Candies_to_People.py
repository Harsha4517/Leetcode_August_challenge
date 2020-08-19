class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        l=[0]*num_people
        r=0
        z=1
        while(1):
            for i in range(num_people):
                if candies<z:
                    l[i]+=candies
                    r=1
                    break
                l[i]+=z
                candies-=z
                z+=1
            if r==1:
                break
        return l
