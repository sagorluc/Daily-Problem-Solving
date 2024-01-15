class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        buy = prices[0]
        
        for i in prices[1:]:
            if i > buy:
                sell = i - buy
                profit = max(profit, sell)
            else:
                buy = i
        return profit

input_arr = list(map(int, input("Enter an array: ").split()))
prices = input_arr
sl = Solution()
res = sl.maxProfit(prices)
print('Total: ', res)

# for i, v in enumerate(input_arr, 1):
#     print('index-',i, 'value-', v)