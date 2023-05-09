a = input()
b = input()
a_l,b_l = len(a),len(b)
lcs = [[0] * (b_l+1) for _ in range(a_l+1)]
for i in range(1,a_l+1):
    for j in range(1,b_l+1):
        if a[i-1] == b[j-1]:
            lcs[i][j] = lcs[i-1][j-1]+1
        else:
            lcs[i][j] = max(lcs[i][j-1],lcs[i-1][j])
print(lcs[-1][-1])
