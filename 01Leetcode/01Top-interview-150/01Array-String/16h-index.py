class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        # print(citations)
        cita_len = len(citations)
        h = 0
        while h < cita_len and citations[h] > h:
            h += 1
            
        return h 
        
       
input_arr = list(map(int, input('Enter an array: ').split())) # 3 0 6 1 5
sl = Solution()
res = sl.hIndex(input_arr)
print('H index is: ', res)