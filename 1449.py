n, l = map(int, input().split())
hole = list(map(int,input().split()))
hole.sort()
last, ans = -1, 0
for a in hole:
  ret = (l-max(0, last-a+1))//l
  last = max(a, last+1)+ret*l-1
  ans += ret
print(ans)