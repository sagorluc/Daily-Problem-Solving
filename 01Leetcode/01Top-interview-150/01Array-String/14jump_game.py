class Solution:
    def canJump(self, nums: list[int]) -> bool:
        last_index = len(nums)-1
        # print(last_index)
        for i in range(len(nums)-2, -1, -1): # reverse iterate form the last second index to first index
           print(i)
           if (i + nums[i]) >= last_index:
               last_index = i
        return last_index == 0
        
        # another solution
        
        # idx = 0
        # for val in nums:
        #     if idx < 0:
        #         return False
        #     elif idx < val:
        #         idx = val
        #         # print(idx)
        #     else:
        #         idx -= val
                
        # return True
           
    
    
input_arr = list(map(int, input('Enter an array: ').split()))
sl = Solution()
res = sl.canJump(input_arr)
if res == True:
    print("Yes. Can jump")
else:
    print("No. Can't jump")