class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right in range(len(nums)):
            # If the window size exceeds k, remove the leftmost element and shrink the window
            if right - left > k:
                window.remove(nums[left])
                left += 1
            
            # If the current element is already in the window, we found a duplicate
            if nums[right] in window:
                return True
                
            # Add the current element to the window
            window.add(nums[right])
            
        return False