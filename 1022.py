dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r1,c1,r2,c2 = map(int,input().split())
board = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]
number = (c2-c1+1) * (r2-r1+1) # 구해야 할 보드 판의 갯수
d = 1 # 방향
x = 0
y = 0
cnt = 1
l = 1
while number>0:
    for _ in range(2):
        for _ in range(l):
            if r1 <= x <= r2 and c1 <= y <= c2:
                number -= 1
                board[x - r1][y - c1] = cnt
                num = cnt
            x += dx[d]
            y += dy[d]
            cnt += 1
        d = (d-1)%4
    l += 1
max_num = len(str(num))
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(board[i][j]).rjust(max_num), end=" ")
    print()