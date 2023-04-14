n = int(input())
len = 1+(4*(n-1))
stardata = [[' ']*len for i in range(len)]
def starpoint(n,idx):
    if n == 1:
        stardata[idx][idx] ='*'
        return
    line = 1+(4*(n-1))
    for i in range(idx,idx+line):
        stardata[idx][i] = '*'
        stardata[idx + line - 1][i] = '*'
        stardata[i][idx] = '*'
        stardata[i][idx + line - 1] = '*'
    starpoint(n-1,idx+2)
starpoint(n,0)

for i in range(len):
    for j in range(len):
        print(stardata[i][j],end ="")
    print()