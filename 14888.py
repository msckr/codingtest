n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = -1e9  # 10억
minimum = 1e9


def cal(total, plus, minus, multi, div, e):
    global maximum, minimum
    if e == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    if plus:
        cal(total + num[e], plus - 1, minus, multi, div, e + 1)
    if minus:
        cal(total - num[e], plus, minus - 1, multi, div, e + 1)
    if multi:
        cal(total * num[e], plus, minus, multi - 1, div, e + 1)
    if div:
        cal(int(total / num[e]), plus, minus, multi, div - 1, e + 1)


cal(num[0], op[0], op[1], op[2], op[3], 1)
print(maximum)
print(minimum)
