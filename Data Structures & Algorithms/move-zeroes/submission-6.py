class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return
        nums.sort(key=bool, reverse=True)