import sys
from collections import deque


def main():
    N, M =map(int, sys.stdin.readline().split())
    graph = [] 
    for _ in range(N):
        graph.append(list(map(int, *sys.stdin.readline().split())))#input())))#sys.stdin.readline())))
        #sys.stdin.readline().split()
    #print(graph)
    visited = [[False]*M for _ in range(N)]

    movement = [(-1,0), (1,0), (0,1), (0,-1)]
    q = deque()
    q.append((0,0,1)) #(x,y,cost)
    a=0
    while q:
        if a>0:
            break
        nx, ny, cost = q.popleft()
        for dx, dy in movement:
            x = nx + dx
            y = ny + dy
            if (0<=x<N) and (0<=y<M) and graph[x][y] == 1 and not visited[x][y]:
                if x == N-1 and y == M-1:
                    print(cost+1)
                    #goto exit
                    a+=1
                    break
                else:
                    visited[x][y] = True
                    q.append((x,y,cost+1))
if __name__ == "__main__":
    main()