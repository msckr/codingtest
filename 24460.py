

N = int(input())
mem = [list(map(int,input().split())) for i in range(N)]
def special(x,y,n):
    if n==1:
        return mem[x][y]
    else:
        sel = [special(x,y,n//2), special(x,y+(n//2),n//2), special(x+(n//2),y,n//2), special(x+(n//2),y+(n//2),n//2)]
        sel.sort()
        return sel[1]
ans = special(0,0,N)
print(ans)