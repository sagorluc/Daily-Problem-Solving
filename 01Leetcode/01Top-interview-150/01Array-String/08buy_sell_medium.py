class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        buy = prices[0]
        
        for i in prices:
            print(i, 'line 7')
            if i < buy:
                buy = i
                print('buy-',buy,'sell-',i, 'line 9')
                
            if i - buy > 0: # avoid nagetive
                profit += (i - buy)
                buy = i
                
        return profit
                



input_arr = list(map(int, input("Enter an array: ").split()))
prices = input_arr
sl = Solution()
res = sl.maxProfit(prices)
print('Total: ', res)