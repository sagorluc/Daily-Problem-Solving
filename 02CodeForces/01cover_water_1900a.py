# problem link-1: https://codeforces.com/problemset/problem/1900/A
# problem link-2: https://codeforces.com/problemset/problem/1792/A
# problem link-3: https://codeforces.com/problemset/problem/2096/A
# problem link-4: https://codeforces.com/problemset/problem/1857/A
# problem link-5: https://codeforces.com/problemset/problem/1761/A
# problem link-6: https://codeforces.com/problemset/problem/2008/C
# problem link-7: https://codeforces.com/problemset/problem/1974/A
# problem link-8: https://codeforces.com/problemset/problem/2005/A
# problem link-9: https://codeforces.com/problemset/problem/1988/B
# problem link-10: https://codeforces.com/problemset/problem/1988/A


def min_water_placements(n, s):
        i = 0
        ans = 0
        count = 0
        while i < n:
            if s[i] == '.':
                count += 1
                ans += 1
            else:
                count = 0
            if count >= 3: break   
            i += 1  
            
        if count >= 3: return 2
        return ans

# -------- Main --------
T = int(input()) # Number of test cases
for _ in range(T):
    n = int(input()) # Length of the string
    s = input()      # The string representing the cells
    results = min_water_placements(n, s)
    print(results)   



# ======================== Problem solution-2 ==========================

# def solve():
#     n = int(input())
#     s = input()

#     # Check for three consecutive empty cells
#     if "..." in s:
#         print(2)  # Placing water in the middle covers all three
#     else:
#         # If no three consecutive empty cells, count all empty cells
#         print(s.count('.'))

# t = int(input())
# for _ in range(t):
#     solve()