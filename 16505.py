import math
N = int(input())
len = pow(2,N)
stardata = [[' ']*len for i in range(len)]
def star(n,x,y):
    if n == 0:
        stardata[0][0]='*'
        return
    for i in range(x,x+len//2):
        for j in range(y,y+len//2):
            stardata[i][y] = '*'
            stardata[x][j] = '*'
    star(n-1,x,y)
    star(n-1,x+len//2,y)
    star(n-1,x,y+len//2)
star(N,0,0)
for i in range(len):
    for j in range(len):
        print(stardata[i][j],end ="")
    print()

