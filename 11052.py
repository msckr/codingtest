N = int(input())
P = [0] + list(map(int,input().split()))
cnt = [0 for _ in range(N+1)]
for i in range(1,N+1):
    for k in range(1,i+1):
        cnt[i] = max(cnt[i],cnt[i-k]+P[k])
print(cnt[i])
