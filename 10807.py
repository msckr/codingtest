n = int(input())
data = list(map(int,input().split()))
v = int(input())
cnt = 0
for i in data:
    if v == i:
        cnt +=1
print(cnt)