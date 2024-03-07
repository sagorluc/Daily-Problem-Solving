class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        dist = set(nums)
        longest = 0
        
        for n in nums:
            # print(n, 'line 7')
            if (n-1) not in dist:
                # print(n, 'line 9')
                length = 1
                while (n+length) in dist:
                    length += 1
                longest = max(longest, length)
        return longest

    
input_arr = list(map(int, input('Enter an array: ').split()))
sl = Solution()
res = sl.longestConsecutive(input_arr)
print('Length of longest consucative is: ', res)