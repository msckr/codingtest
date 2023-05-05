import math
N = int(input())
len = pow(2,N)
stardata = [[' ']*len for i in range(len)]
def star(n,x,y):
    if n == 0:
        stardata[x][y]='*'
        return
    star(n-1,x,y)
    star(n-1,x+pow(2,n-1),y)
    star(n-1,x,y+pow(2,n-1))
star(N,0,0)
for i in range(len):
    for j in range(len-i):
        print(stardata[i][j],end ="")
    print()