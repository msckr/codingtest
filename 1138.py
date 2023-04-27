N = int(input())
m = list(map(int,input().split()))
person = [0] * N
for i in range(1,N+1):
    t = m[i-1]
    cnt = 0
    for j in range(N):
        if cnt == t and person[j] == 0:
            person[j] = i
            break
        elif person[j] == 0:
            cnt+=1
print(*person)