class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r,l=1,0
        maxp=0
        while r<len(prices):
            if prices[l]>prices[r]:
                l=r
            maxp=max(maxp,prices[r]-prices[l])
            r+=1
        return maxp






        