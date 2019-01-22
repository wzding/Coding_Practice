
# bidirectional
from collections import deque

def doubleBFS(start, end):
    if start == end:
        return 1
    
    # 分别从起点和终点开始的两个BFS队列
    startQueue, endQueue = deque(), deque()
    startQueue.append(start)
    endQueue.append(end)
    step = 0
    
    # 从起点开始和从终点开始分别访问过的节点集合
    startVisited, endVisited = set(), set()
    startVisited.add(start)
    endVisited.add(end)
    while len(startQueue) and len(endQueue):
        startSize, endSize = len(startQueue), len(endQueue)
        #　按层遍历
        step += 1
        for _ in range(startSize):
            cur = startQueue.popleft()
            for neighbor in cur.neighbors:
                if neighbor in startVisited: # 重复节点
                    continue
                elif neighbor in endVisited: # 相交
                    return step
                else:
                    startVisited.add(neighbor)
                    startQueue.append(neighbor)
        step += 1
        for _ in range(endSize):
            cur = endQueue.popleft()
            for neighbor in cur.neighbors:
                if neighbor in endVisited:
                    continue
                elif neighbor in startVisited:
                    return step
                else:
                    endVisited.add(neighbor)
                    endQueue.append(neighbor)
    
    return -1
