class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            if nums[mid] < nums[mid + 1]:
                # Ascending slope: peak lies to the right
                low = mid + 1
            else:
                # Descending slope: mid could be a peak or peak is to the left
                high = mid
                
        return low