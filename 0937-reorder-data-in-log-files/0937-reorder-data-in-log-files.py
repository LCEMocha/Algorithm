class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig = []
        let = []
    
        for i in logs:
            if i.split()[1].isdigit():
                dig.append(i)
            else:
                let.append(i)
            
        let.sort(key=lambda x:(x.split()[1:], x.split()[0]))
        #dig.sort(key=lambda x:(x.split()[1:], x.split()[0]), reverse=True)
        
        return(let+dig)