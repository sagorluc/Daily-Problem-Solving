def solve():
    n = int(input())
    m = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if m[i] == 1:
            count += 1
    print(int(n - (count // 2)))

T = int(input())
for _ in range(T):
    solve()
