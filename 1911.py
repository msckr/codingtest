import sys
sys.setrecursionlimit(1000000)
N,L = map(int,sys.stdin.readline().split())
lake = []
for _ in range(N):
    lake.append(list(map(int, sys.stdin.readline().split())))
lake.sort()
cnt = 0
for pool in range(len(lake)):
    l = lake[pool][1]-lake[pool][0]
    if pool == len(lake)-1:
        cnt +=  (l-1)//L +1
        break
    if (l) % L:
        tmp = L - ((l)% L)
        now_corver = lake[pool][1] + tmp
        if lake[pool+1][0] <=now_corver :
            lake[pool+1][0] = now_corver
        cnt += (l)//L +1
    else :
        cnt += (l)//L
print(cnt)
#시간초과
# for start, end in lake:
#     if start > end:
#         continue
#     if now > start:
#         start = now
#     while start < end:
#         start += L
#         cnt += 1
#     now = start
# print(cnt)