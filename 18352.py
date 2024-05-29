import sys
from collections import deque

def main():
    N, M, K, X = map(int, sys.stdin.readline().split())

    graph = [[]*i for i in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)

    ans = []
    depth = 0
    visited = [False]*(N+1)
    dq = deque()
    dq.append([X,0])
    visited[X] = True

    while dq:
        v, d = dq.popleft()
        for item in graph[v]:
            if not visited[item]:
                dq.append([item,d+1])
                visited[item] = True
                if d+1 == K:
                    ans.append(item)

    if len(ans)==0:
        print(-1)
    else:
        ans  = sorted(ans)
        for answer in ans:
            print(answer)

def bfs(graph, start):
    answer=[]
    visited = [False] * (len(graph)+1)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        #print(v, end='')
        answer.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return answer

if __name__ == "__main__":
    main()