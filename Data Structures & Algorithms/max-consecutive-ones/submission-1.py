class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxstreak = 0
        for i in nums:
            if i == 1:
                count += 1
                maxstreak = max(count, maxstreak)
            else:
                count = 0
        return maxstreak