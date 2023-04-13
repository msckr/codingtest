import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums =[sys.stdin.readline().strip() for i in range(n)]
    nums.sort()
    check = True
    for i in range(n-1):
        felix = len(nums[i])
        if nums[i] == nums[i+1][:felix]:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")
