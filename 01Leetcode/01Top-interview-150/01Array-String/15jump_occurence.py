class Solution:
    def jump(self, nums: list[int]) -> bool:
        occur = 0
        end = 0
        farest = 0
        last_index = len(nums)-1
        # print(last_index) # index 4
        # print(nums[last_index]) # value 4
        for i in range(last_index):
            farest = max(farest, i+nums[i]) # taking the max 
            
            if farest >= last_index: # trying to reach last index
                # print(farest)
                occur += 1
                break
            
            if i == end:  # jodi first level ei peye jai
                occur += 1
                end = farest
                # print(end)
            
            # print(farest, end)
                
        return occur
                
        
input_arr = list(map(int, input('Enter an array: ').split())) # 2 3 0 1 4
sl = Solution()
res = sl.jump(input_arr)
print('Total jump: ', res)