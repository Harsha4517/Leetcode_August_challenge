class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        r=len(citations)
        for i in citations:
            if r<=i:
                return r
            r-=1
        return 0
