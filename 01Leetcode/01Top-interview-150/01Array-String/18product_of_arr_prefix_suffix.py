class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        # print(ans) # [0, 0, 0, 0]
        prefix = 1
        postfix = 1
        len_arr = len(nums)
        
        for i in range(len_arr):
            ans[i] = prefix 
            # print(ans[i], prefix) # 1 1 1 1
            prefix = prefix * nums[i] 
            # print(ans[i],prefix, 'line 13') # ans[i]= 1 1 2 6, prefix= 1 2 6 24
            
        for i in range(len_arr-1, -1, -1): # reverse index 3 2 1 0
            # print(i)
            ans[i] = ans[i] * postfix
            # print(ans[i],postfix) # ans[i] = 6 2 1 1, postfix= 1 1 1 1
            postfix = postfix * nums[i]
            # print(ans[i], postfix, 'line 20') # ans[i]= 6 8 12 24, postfix= 4 12 24 24 
            
        return ans
    
    
input_arr = list(map(int, input("Enter an array: ").split())) # 1 2 3 4
sl = Solution()
res = sl.productExceptSelf(input_arr)
print('All the product equal to: ', res)
