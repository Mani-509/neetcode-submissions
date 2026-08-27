class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num={}
        res=[]
        for nu in nums:
            if nu in num:
                num[nu]+=1
            else:
                num[nu]=1
        for i in range(1,len(nums)+1):
            if i not in nums:
                res.append(i)
        return res 
    