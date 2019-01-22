# 不需分层
from collections import deque

queue = deque()
seen = set()  #等价于Java版本中的set

seen.add(start)
queue.append(start)
while len(queue):
    head = queue.popleft()
    for neighbor in head.neighbors:
        if neighbor not in seen:
            seen.add(neighbor)
            queue.append(neighbor)

# 分层
from collections import deque

queue = deque()
seen = set()

seen.add(start)
queue.append(start)
while len(queue):
    size = len(queue)
    for _ in range(size):
        head = queue.popleft()
        for neighbor in head.neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
