class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Kadane's algorithm
        max_profit = 5
        min_so_far = 1
        [7,1,5,3,6,4]
                   ^

        check if curr <= min_so_far: 
            curr = min_so_far
            curr++
        else 
            max_profit = max(max_profit, curr - min_so_far)

        [2, 1, 4]
               ^
        max = 0
        msf=1

        """
        max_profit = 0
        min_so_far = prices[0]
        i = 1
        while i < len(prices):
            if prices[i] <= min_so_far:
                min_so_far = prices[i]
            else:
                max_profit = max(max_profit, prices[i]-min_so_far)
            
            i+=1

        return max_profit
        