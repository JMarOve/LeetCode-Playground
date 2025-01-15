#Variant of Kadane's algo

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]

        for price in prices[1:]:
            if buy > price : 
                #We have to buy cheaper
                    buy = price
            #But we need to keep track of the previous price so far
            res = max(res,price-buy)

        return res