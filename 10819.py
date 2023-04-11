from itertools import permutations

n = int(input())
m = list(map(int,input().split()))
m.sort()
ans = 0
per = permutations(m)
for i in per:
    s = 0
    for j in range(len(i)-1):
        s+= abs(i[j]-i[j+1])
    if s > ans:
        ans = s
print(ans)
