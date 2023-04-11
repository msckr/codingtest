import math
a,b = map(int,input().split())
List = [0] * (int(math.sqrt(b))+1)
List[2] = 2
cnt = 0
for i in range(3,len(List),2):
    List[i] = i
for i in range(3,int(math.sqrt(b))+1,2):
    if List[i] == 0:
        continue
    for j in range(i+i,int(math.sqrt(b))+1,i):
        List[j]=0

for i in range(2,int(math.sqrt(b))+1):
    if List[i]!=0:
        temp = List[i]
        while List[i] <= b/temp:
            if List[i] >= a/temp:
                cnt +=1
            temp = temp*List[i]
print(cnt)