# Solution 1 - (책 풀이)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # 직렬화 
    def serialize(self, root):
        queue = collections.deque([root])
        result = ['#'] # 직렬화 결과를 저장하는 리스트 
        
        # queue에서 연결된 노드들을 하나씩 pop하여 result 배열에 추가함
        while queue:
            node = queue.popleft()
            if node : 
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
                
            else: 
                result.append('#') # 노드에 값이 없으면 #로 표기한다. 
            
        return ''.join(result)
    
    
    # 역직렬화 
    def deserialize(self, data):
        # 예외 처리 
        if data == '# #' : 
            return None
        
        # 공백을 기준으로 문자열을 split
        node = data.split()
   
        # Root 노드는 따로 빼서 TreeNode로 지정해준다. 
        root = TreeNode(int(node[1]))
        queue = collections.deque([root]) # 큐에는 루트 노드부터 연결된 노드들이 들어간다.
        index = 2 # node 리스트에서 하나씩 접근하는 인덱스
        

        # 큐룰 돌며 연결된 노드들을 저장한다. 
        while queue : 
            node = queue.popleft()
            
            if node[index] is not '#' :
                node.left = TreeNode(int(node[index]))
                queue.append(node.left)
            index += 1
            
            if node[index] is not '#' :
                node.right = TreeNode(int(node[index]))
                queue.append(node.right)
            index += 1
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# 풀이 : (주석 참고) 
# 부가 설명 : "직렬화"는 '이진 트리' 라는 논리적인 구조를 파일이나 디스크에 저장하기 위해 물리적인 형태로 바꾸는 것을 말한다. 
# 후기 : 이진트리를 문자열로 바꾸는 직렬화와 그 반대인 역직렬화 원리를 기억하며 코드를 작성하고 기억해야겠다. 