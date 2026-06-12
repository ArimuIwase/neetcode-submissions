class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        lists=[]
        output=[]
        for i in nums:
            hm.setdefault(i,0)
            hm[i]+=1
        for key in hm.keys():
            lists.append([hm[key],key])
        ordered = sorted(lists, key=lambda x:x[0])
        for _ in range(k):
            val, key = ordered.pop()
            output.append(key)
            
            
        print (lists)
        print (hm)
        print (output)
        return output

    
