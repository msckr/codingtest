N = int(input())
lst = list(map(int,input().split()))
K = int(input())

def f(lst, N, K):
    if K == 1:
        lst.sort()
        print(" ".join(map(str, lst)), end=" ")
    else:
        f(lst[:N//2], N//2, K//2)
        f(lst[N//2:], N//2, K//2)
f(lst,N,K)