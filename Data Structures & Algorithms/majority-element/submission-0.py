class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=sorted(nums)
        return m[len(nums)//2]
        