from itertools import combinations
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.d=list(combinations(list(characters),combinationLength))
        self.i=0

    def next(self) -> str:
        self.i+=1
        return ''.join(self.d[self.i-1])
    

    def hasNext(self) -> bool:
        if self.i==len(self.d):
            return False
        return True

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
