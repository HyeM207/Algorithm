# Solution 1
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        words = {}
        
        for para in paragraph.split():
            para = para.lower()
            para = re.split(r'\,',para)  
            
            for word in para : 
                if word != '':
                    word = re.sub('[^a-z]', '', word)

                    if word in banned : 
                        pass
                    else: 
                        if word in words : 
                            words[word] += 1
                        else : 
                            words[word] = 1

        # print(words)
        return max(words, key=words.get) 