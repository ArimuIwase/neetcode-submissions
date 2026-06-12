class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            nums2= nums.copy()
            nums2.pop(i)
            p=1
            for j in nums2:
                p= p*j
            res.append(p) 
        return res