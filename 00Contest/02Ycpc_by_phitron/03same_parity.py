def same_parity():
    n = int(input())
    m = list(map(int, input().split()))
    flag = False
    for _ in range(n):
        if len(m) % 2 != 0:
            flag = True
    
    if not flag:
        print("YES")
    else:
        print("NO")
        
T = int(input())
for _ in range(T):
    same_parity()