N,L = map(int,input().split())
lake = [list(map(int,input().split())) for _ in range(N)]
lake.sort()
num = 0
for pool in range(len(lake)):
    l = lake[pool][1] - lake[pool][0]
    if pool == len(lake) + 1:
        num+=(l-1)/L+1
        break
    if (l%L):
        tmp = L -((l)%L)
        now = lake[pool][1]+tmp
        if lake[pool+1][0] <= now:
            lake[pool+1][0] = now
        num += (l)//L+1
    else:
        num += l/L
print(int(num))
