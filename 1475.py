import  heapq
N = int(input())
card = []
for _ in range(N):
    h = int(input())
    card.append(h)
heapq.heapify(card)
cnt = 0
while len(card) > 1:
    temp1 = heapq.heappop(card)
    temp2 = heapq.heappop(card)
    cnt += temp1 + temp2
    heapq.heappush(card, temp1 + temp2)
print(cnt)