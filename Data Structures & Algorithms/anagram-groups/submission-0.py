class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        out=[]
        for i in strs:
            j= "".join(sorted(i))
            hm.setdefault(j, [])
            hm[j].append(i)
        for keys in hm:
            out.append(hm[keys])
        return out


        