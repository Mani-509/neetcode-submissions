class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 1. Filter non-zeros into a list
        # 2. Append zeros to match original length
        # 3. Update nums in-place using slice assignment
        nums[:] = [x for x in nums if x != 0] + [0]* nums.count(0)