class Solution(object):
    def removeElement(self, nums, val): 
        idx = 0     
        for i in range(0, len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[idx] = nums[i]
                # print(nums[idx], 'line 9') # value of array
                idx += 1
                # print(idx, 'line 10') # index of array
        return idx
        
        
        
input_arr = list(map(int, input('Enter the array: ').split()))
val = int(input('Enter the number to remove: '))

sl = Solution()
res = sl.removeElement(input_arr, val)
print(res, 'line15')
print('After remove the element: ', input_arr[:res])