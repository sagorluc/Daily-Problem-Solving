class Solution(object):
    def majorityElement(self, nums):
        # nums.sort()
        # len_num = len(nums)
        # return nums[len_num // 2]

      
        # this solution is getting runtime error
        occur = 1
        mxx_occur = 1
        nums.sort()
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                occur += 1
            else:
                occur = 1
                
            mx_occur = max(mxx_occur, occur)
        # print(mx_occur+1)
        return nums[(mx_occur+2) // 2]
        

n = int(input('Enter a number: '))        
input_arr = list(map(int, input('Enter a array: ').strip().split()))[:n]
sl = Solution()
res = sl.majorityElement(input_arr)
print('Majority element is: ', res)
# print('Majority element is: ', input_arr[:res])