# 풀이1 (240102) : 성공 - 검색하면서 풀음
"""
직접 Node와 BinaryTree, 전위/후위 순회 구현함
 - 재귀함수 깊이 조절해줘야됨 (안 하면 런타임오류뜸)
"""
from sys import setrecursionlimit
setrecursionlimit(10000)

class Node():
    def __init__(self, node): 
        self.x = node[0]
        self.y = node[1]
        self.node_idx = node[2]
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
        
    def insert(self, newnode):
        self.root = self._insert(self.root, newnode)
        return self.root is not None

    def _insert(self, node, newnode):
        if node is None:
            return newnode

        if newnode.x < node.x:
            node.left = self._insert(node.left, newnode)
        else:
            node.right = self._insert(node.right, newnode)
        return node
        
def solution(nodeinfo):
    answer = [[], []]
    
    # 1. 노드 번호 추가 및 level 내림차순 정렬
    nodes = []
    for node_num, node in enumerate(nodeinfo):
        nodes.append(node + [node_num + 1])
    
    nodes.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    tree = BinaryTree()

    # 2. 이진트리 만들기
    for node in nodes:
        tree.insert(Node(node))

    # 3-1. 전위 탐색 구현 (중앙 -> 왼 -> 오)
    def preorder(node):
        if node:
            answer[0].append(node.node_idx)
            preorder(node.left)
            preorder(node.right)

    # 3-2. 후위 탐색 구현 (왼->오->중앙)
    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            answer[1].append(node.node_idx)

    # 3. 탐색하기
    preorder(tree.root)
    postorder(tree.root)
    
    return answer
