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
        state = bfs(graph, N, M)
        if state == 2:
            print(0)
            break
        elif state == 0:
            print(ans)
            break
        else:
            graph = melt_ice(graph, N, M)
            ans += 1

def bfs(graph, N, M):
    visited = [[False] * M for _ in range(N)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    start = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                visited[i][j] = True
            else:
                start.append((i, j))
    
    if len(start) <= 1:
        return 2

    q = deque([start[0]])
    visited[start[0][0]][start[0][1]] = True
    components = 1

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                components += 1

    return 1 if components == len(start) else 0

def melt_ice(graph, N, M):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    new_graph = [row[:] for row in graph]

    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                water_count = sum(1 for dx, dy in directions if 0 <= i + dx < N and 0 <= j + dy < M and graph[i + dx][j + dy] == 0)
                new_graph[i][j] = max(graph[i][j] - water_count, 0)
    
    return new_graph

if __name__ == "__main__":
    main()