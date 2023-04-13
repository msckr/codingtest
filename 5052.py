t=int(input())
for _ in range(t):
    n = int(input())
    nums = [input() for _ in range(n)]
    nums.sort()
    check = True
    for i in range(n-1):
        felix = len(nums[i])
        if nums[i] == nums[i+1][:felix]:
            check = False
    if check:
        print("YES")
    else:
        print("NO")
