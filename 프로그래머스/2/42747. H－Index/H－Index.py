def solution(citations):
    citations.sort()        
    for i in range(len(citations)-1, -1, -1):
        count = 0
        point = len(citations)-1
        while point >= 0:
            if citations[point] >= i+1:
                count += 1
                point -= 1
            else: 
                break
        print(count)
        if count >= i+1 and len(citations)-count <= i+1:
            return i+1
    return 0