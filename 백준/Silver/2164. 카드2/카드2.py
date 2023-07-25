from collections import deque

# initialize queue
q = deque()
card = int(input())
# fill in the queue
for i in range(card):
  q.append(i+1)

while len(q) > 1:
  q.popleft()
  next_item = q.popleft()
  q.append(next_item)
print(q[0])
  