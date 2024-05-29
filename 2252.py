import sys
from collections import deque

def main():
    N, M = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(N+1)]
    into_dim = [0]*(N+1)
    
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        into_dim[b]+=1
    #print(graph)
    #print(into_dim)

    visited = [False] * (len(graph)+1)
    queue = deque()
    for i in range(1, N+1):
        if into_dim[i] == 0: #진입 차수가 0
            queue.append(i)
            visited[i] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        #print(graph[v])
        for i in graph[v]:
            if not visited[i]:
                if into_dim[i]==1:
                    into_dim[i]-=1
                    queue.append(i)
                    visited[i] = True
                else:
                    into_dim[i]-=1



if __name__ == "__main__":
    main()