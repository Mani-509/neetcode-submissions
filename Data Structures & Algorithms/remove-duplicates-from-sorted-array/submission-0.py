class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r=0
        l=0
        while l<len(nums):
            if nums[r]!=nums[l]:
                r+=1
                nums[r],nums[l]=nums[l],nums[r]
            l+=1
        
        return len(set(nums))


        