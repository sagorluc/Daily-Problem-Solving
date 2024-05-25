# problem link: https://www.hackerrank.com/contests/ycpc-by-phitron-1st-round-beginner-level-contest-1-2024-1/challenges/toggle-switch

import math

T = int(input('Enter an test case>> '))

for ts in range(T):
    n = int(input('Enter n>> ').strip())
    # print(n)
    ans = math.floor(math.sqrt(n))
    print(ans)