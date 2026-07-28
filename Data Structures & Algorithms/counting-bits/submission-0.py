class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            res.append(self.countones(i))
        return res

    def countones(self,m):
        res = 0
        while m > 0:
            m &= (m - 1)  # Drops the lowest set bit
            res += 1
        return res
        