class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        
        # 1. Shift all non-zero elements to the front
        for x in nums:
            if x != 0:
                nums[j] = x
                j += 1
        
        # 2. Fill the rest with zeros
        while j < len(nums):
            nums[j] = 0
            j += 1