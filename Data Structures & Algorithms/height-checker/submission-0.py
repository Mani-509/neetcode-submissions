class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        nums=sorted(heights)
        j=0
        i=0
        count=0
        while j<len(heights) and i<len(heights):
            if nums[i]!=heights[j]:
                count+=1
            j+=1
            i+=1
        return count 