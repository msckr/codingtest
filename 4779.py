def can(n,idx,temp):
    if n == 0:
        return
    line = 3 ** (n-1)
    for i in range(idx +line,idx + 2*line):
        ans[i] = ' '
    can(n-1,idx,idx+line-1)
    can(n-1,idx+(line*2),idx+(3*line) -1)

while True:
    try:
        n = int(input())
        num = 3 ** n
        ans = ['-'] * num
        can(n, 0, num - 1)
        print("".join(ans))
    except EOFError:
        break


