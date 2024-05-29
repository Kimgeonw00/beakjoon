import sys
from collections import deque


def main():
    N = int(sys.stdin.readline())
    link = int(sys.stdin.readline())
    graph = [[] for _ in range(N+1)]
    for i in range(link):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    #print(graph)

    q = deque()
    answer = [1]
    q.append(1)

    while q:
        k = q.popleft()
        for item in graph[k]:
            if item not in answer:
                answer.append(item)
                q.append(item)
    print(len(answer)-1)


def main2():
    N = int(sys.stdin.readline())
    link = int(sys.stdin.readline())
    graph = [[] for _ in range(N+1)]
    for i in range(link):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    stack = []
    stack.append(1)
    answer = [1]

    while stack:
        #k = stack[-1]
        #stack.remove(k)
        k = stack.pop()
        for item in graph[k]:
            if item not in answer:
                answer.append(item)
                stack.append(item)
    print(len(answer)-1)

def main3():
    N = int(sys.stdin.readline())
    link = int(sys.stdin.readline())
    graph = [[] for _ in range(N+1)]
    for i in range(link):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    answer = [1]
    again(graph, answer, 1)

    print(len(answer)-1)

def again(graph, answer, cur):
    for item in graph[cur]:
        if item not in answer:
            answer.append(item)
            again(graph, answer, item)


if __name__ == "__main__":
    main3()