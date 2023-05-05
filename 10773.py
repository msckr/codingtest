K = int(input())
number=[]
for _ in range(K):
    h = int(input())
    if (h==0):
        number.pop()
    else :
        number.append(h)
ans = 0
for i in number:
    ans += i
print(ans)