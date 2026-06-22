class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        mprofit=0
        for r in range(len(prices)):
            while prices[l]>prices[r]:
                l+=1
            if prices[r]-prices[l] > mprofit:
                mprofit= prices[r]-prices[l]
       
        return mprofit
             

        