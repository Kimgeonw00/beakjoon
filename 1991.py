import sys

def main():
    N = int(sys.stdin.readline())
    tree = {} #숫자가 아니라 dic으로 가야함
    for i in range(N):
        root, left, right = sys.stdin.readline().split()
        tree[root] = [left, right]

    preorder(tree, "A")
    print()
    inorder(tree, "A")
    print()
    postorder(tree,"A")

def preorder(graph, root):
    print(root, end='')
    if graph[root][0]!=".":
        preorder(graph, graph[root][0])
    if graph[root][1]!=".":
        preorder(graph, graph[root][1])

def inorder(graph, root):
    if graph[root][0]!=".":
        inorder(graph, graph[root][0])
    print(root, end='')
    if graph[root][1]!=".":
        inorder(graph, graph[root][1])

def postorder(graph, root):
    if graph[root][0]!=".":
        postorder(graph, graph[root][0])
    if graph[root][1]!=".":
        postorder(graph, graph[root][1])
    print(root, end='')

if __name__ == "__main__":
    main()