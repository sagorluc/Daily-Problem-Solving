class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left, total = 0, 0
        ans = float("inf")
        
        # Sliding window
        for right in range(len(nums)):
            total += nums[right] # adding the right value
            while total >= target:
                total -= nums[left] # substruct from the left value
                ans = min(right - left + 1, ans)
                left += 1
                
        if ans == float("inf"):
            return 0
        else:
            return ans
        
    
 
input_arr = list(map(int, input("Enter a array: ").split()))
target = int(input("Enter a number: ")) 
sl = Solution()
res = sl.minSubArrayLen(target, input_arr)
print("Minimum sub array is: ", res)