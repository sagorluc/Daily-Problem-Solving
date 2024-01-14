
class Solution(object):
    def rotate(self, nums, k):
        
        def rev(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l] # reverse the array
                l += 1
                r -= 1
                
        n = len(nums) # if length 6
        k = k % n # remain 2
        rev(0, n-1) # reverse the entire array
        rev(0, k-1) # reverse the k-th element
        rev(k, n-1) # reverse the remain array
                
        
        

input_arr = list(map(int, input('Enter an array: ').split()))
input_k = int(input("Enter a number: "))
sort_arr = sorted(input_arr)
sl = Solution()
res = sl.rotate(sort_arr, input_k)
print('After rotate array: ', sort_arr)