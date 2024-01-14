class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for x in range(n):
            nums1[m+x] = nums2[x] 
        return nums1.sort()
                
    
a = int(input('Enter a number: '))
b = int(input('Enter second number: '))

input1 = list(map(int, input("Enter Array1 : ").strip().split()))[:a+b]
input2 = list(map(int, input("Enter Array2 : ").strip().split()))[:b]
    

print(input1, 'line 26')
print(input2, 'line 27')
  
sl = Solution()
sl.merge(input1, a, input2, b)
print(input1)    