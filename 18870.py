N = int(input())
x = list(map(int,input().split()))
xlist= sorted(list(set(x)))
cnt = {xlist[i] : i for i in range(len(xlist))}
for i in x:
    print(cnt[i],end=' ')