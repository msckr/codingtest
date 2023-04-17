A = int(input())
a = list(map(int,input().split()))
cnt = [0 for _ in range(A)]
for i in range(A):
    for j in range(A):
        if a[i]>a[j] and cnt[i]<cnt[j]:
            cnt[i] = cnt[j]
    cnt[i] += 1
print(max(cnt))