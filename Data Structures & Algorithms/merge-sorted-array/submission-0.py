class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Last index of nums1's valid elements
        p1 = m - 1
        # Last index of nums2
        p2 = n - 1
        # Last index of the total space in nums1
        right = m + n - 1
        
        # While there are still elements to process in nums2
        while p2 >= 0:
            # If nums1 still has elements and its current element is bigger
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[right] = nums1[p1]
                p1 -= 1
            else:
                # Otherwise, take the element from nums2
                nums1[right] = nums2[p2]
                p2 -= 1
            
            # Move our placement pointer backwards
            right -= 1