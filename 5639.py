import sys

sys.setrecursionlimit(2*10**5)

def main():
    #N = int(input())
    tree =  Tree()
    #tree = {} #숫자가 아니라 dic으로 가야함
    #for i in range(N):
    #    root, left, right = sys.stdin.readline().split()
    #    tree[root] = [left, right]

    #print(N)
    while True:
        try:
            new_node = int(input())
            tree.push(new_node)
            #binary_search_tree.append(new_node)
        except:
            break
    tree.postorder(tree.root)


class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root = None):
        self.root = root

    def push(self, value):
        node = Node(value=value)
        tempNode = self.root

        if self.root == None:
            self.root = node
            return
        else:
            ptrNode = self.root #포인터 노드라고 할 수 있겠다
            while ptrNode != None:
                tempNode = ptrNode
                if node.value < ptrNode.value:
                    ptrNode = ptrNode.left
                else:
                    ptrNode = ptrNode.right
            
            if node.value < tempNode.value:
                tempNode.left = node
            else:
                tempNode.right = node

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)

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