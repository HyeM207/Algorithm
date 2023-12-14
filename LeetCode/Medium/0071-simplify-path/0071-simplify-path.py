class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        1. split()으로 // 혹은 /로 구분 및 . 제외하여 path 담기
        2. 디렉토리 이름이 ..이면 처리해주기
        
        testcase: "/a/./b/../../c/"
        """
        split_path = [p for p in path.split('/') if p and p != '.']
        stack = []
        
        for directory in split_path:
            if directory == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(directory)
        result = '/' + '/'.join(stack)
        return result if result else '/'
        
        