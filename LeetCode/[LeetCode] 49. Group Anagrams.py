# Solution 1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     
        output = []
        anagrams = {} # dictionay for check anagram's Index in 'output' list
        insertIdx = 0
        
        for _str in strs :   
            sortedStr = "".join(sorted(_str))
            
            if sortedStr in anagrams : 
                output[anagrams[sortedStr]].append(_str)
            else :
                anagrams[sortedStr] = insertIdx
                output.insert(insertIdx, [_str])
                insertIdx += 1
         
                
        return output


# Solution 2
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     
        anagrams = collections.defaultdict(list)
        
        for word in strs : 
        	anagrams[''.join(sorted(word))].append(word)
            
        return list(anagrams.values())