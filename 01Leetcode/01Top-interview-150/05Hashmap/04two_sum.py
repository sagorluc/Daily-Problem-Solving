class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ## hash table solution
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i # {3: 0, 2: 1, 4: 2}
        # print(numMap)
        
        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            # print(complement, 'line 15')            # 3, 4
            # print(numMap, 'line 16')                # {3: 0, 2: 1, 4: 2}
            # print(numMap[complement], 'line 17')    # 0, 2
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found
        
        
        ## two pointer solution
        # nums.sort()
        # st = 0
        # last = len(nums)-1
        # len_nums = len(nums)
        # ans = []
        # for i in range(len_nums):
        #     if nums[st] + nums[last] == target:
        #         ans = [st, last]
        #     elif nums[st] + nums[last] > target:    
        #         last -= 1
        #     else:
        #         st += 1
                 
        # return ans
    
    
input_arr = list(map(int, input('Enter an array: ').split()))
input_target = int(input("Enter a number: "))

sl = Solution()
res = sl.twoSum(input_arr, input_target)
print("Index of two sum is: ", res)
