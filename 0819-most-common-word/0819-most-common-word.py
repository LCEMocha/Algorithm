class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        
        #정규식을 사용함으로써 구두점 제거
        #구두점으로 인해 isalnum()은 사용할 수 없다. ex) 'ball,' == False
        
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() 
                 if word not in banned]
        count = collections.Counter(words)
        most = count.most_common(1)
        return most[0][0]
        