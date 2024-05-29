import sys
from collections import deque

def main():
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])

    graph = []
    idx = 2
    for _ in range(N):
        graph.append(list(map(int, data[idx:idx + M])))
        idx += M

    ans = 0
    while True:
        a = bfs(graph, N, M)
        if a==2:
            print(0)
            break
        elif a==0:
            print(ans)
            break
        else:
            graph = year(graph, N, M)
            ans+=1

def bfs(graph, row, col):
    #row = len(graph)
    #col = len(graph[0])
    visited = [[False]*col for _ in range(row)]
    move = [(1,0),(-1,0),(0,1),(0,-1)]

    start = []
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 0:
                visited[i][j] = True
            else:
                start.append([i,j])
    if len(start)<=1:
        return 2

    q = deque([start[0]])
    #q.append(start[0])
    #start = start[1:]
    visit=1
    visited[start[0][0]][start[0][1]] = True
    
    while q:
        nx, ny = q.popleft()
        for dx, dy in move:
            x = nx + dx
            y = ny + dy
            if (0<=x<row) and (0<=y<col) and graph[x][y] != 0 and not visited[x][y]:
                visited[x][y] = True
                q.append([x,y])
                visit+=1
    
    if len(start)==visit:
        return 1
    else:
        return 0

def year(graph, row, col):
    #row = len(graph)
    #col = len(graph[0])
    copy_graph =  [[0]*col for _ in range(row)]
    #[[0 for _ in range(col)] for _ in range(row)]
    move = [(1,0),(-1,0),(0,1),(0,-1)]

    for i in range(row):
        for j in range(col):
            if graph[i][j] != 0:
                water = sum(1 for dx, dy in move if 0 <= i + dx < row and 0 <= j + dy < col and graph[i + dx][j + dy] == 0)
                """for dx, dy in move:
                    x = i + dx
                    y = j + dy
                    if (0<=x<row) and (0<=y<col) and graph[x][y]==0:
                        water+=1"""
                copy_graph[i][j] = max(0,graph[i][j]-water)
    return copy_graph
if __name__ == "__main__":
    main()