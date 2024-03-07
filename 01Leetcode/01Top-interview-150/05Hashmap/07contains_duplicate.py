class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        left = 0
        
        # Sliding window
        for right in range(len(nums)):
            # base case
            if right - left > k:
                window.remove(nums[left])
                left += 1
                
            if nums[right] in window:
                return True
            else:
                window.add(nums[right])

        return False
    
input_arr = list(map(int, input('Enter an array: ').split()))
target_value = int(input('Enter an target value: '))
sl = Solution()
res = sl.containsNearbyDuplicate(input_arr, target_value)
print('Is contains near by duplicate: ', res)        