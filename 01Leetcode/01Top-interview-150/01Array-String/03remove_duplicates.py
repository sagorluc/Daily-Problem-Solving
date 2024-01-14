class Solution(object):
    def removeDuplicates(self, nums):
        idx = 1
        for i in range(1, len(nums)):
            print('index--',i, 'value--', nums[i], '-- line 5')
            if nums[i-1] != nums[i]:
                nums[idx] = nums[i]
                idx += 1
        return idx
            
        
        
input_arr = list(map(int, input("Enter an array: ").split()))
sort_arr = sorted(input_arr)
sl = Solution()
res = sl.removeDuplicates(sort_arr)
print('Length of array is ', res)
print('Remain the number is: ', sort_arr[:res])
