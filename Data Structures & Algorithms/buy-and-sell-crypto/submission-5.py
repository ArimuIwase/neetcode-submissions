class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        outputs=[]
        for r in range(len(prices)):
            while prices[l]>prices[r]:
                l+=1
            outputs.append(prices[r]-prices[l])
            print(outputs)
       
        if outputs==[]: return 0
        return max(outputs)
             

        