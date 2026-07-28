
class Solution:
    def hammingWeight(self, n: int) -> int:
        m=bin(n)
        res=0
        for ch in m:
            if ch=="1":
                res+=1
        return res 
        