class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm={}
        if nums==[]: return 0
        for i in set(nums):
            if i-1 not in set(nums):
                hm[i]=[]
        for start in hm.keys():
            count= start
            while count in set(nums):
                hm[start].append(count)
                count +=1
        print(hm)
        s=set()
        for value in hm.values():
            s.add(len(value))
        return max(s)



