# Solution 1 
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []
        
        
        for log in logs : 
            if log.split()[1].isalpha() == True :
                letterLogs.append(log)
            else : 
                digitLogs.append(log)
            

        letterLogs = sorted(letterLogs, key=lambda a : (a.split()[1:], a.split()[0]))
        
        return letterLogs + digitLogs