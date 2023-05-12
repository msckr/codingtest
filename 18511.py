from itertools import product

N, K = map(int, input().split())
N_len = len(str(N))
k_list = list(input().split())

while True:
    tmp = list(product(k_list,repeat = N_len))
    result = []

    for i in tmp:
        if int("".join(i)) <= N:
            result.append(int("".join(i)))

    if len(result) >= 1:
        print(max(result))
        break

    else:
        N_len -= 1

