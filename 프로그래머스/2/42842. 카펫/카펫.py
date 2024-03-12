def solution(brown, yellow):
    answer = []
    root = int((brown+yellow)**(1/2))
    div = (brown+yellow)//root
    while 1>0:
        if (div*2) + (root*2) - 4 == brown :
            answer.append(div)
            answer.append(root)
            return answer
        else:
            root -= 1
            if root>0 and (brown+yellow)%root == 0:
                div = (brown+yellow)//root
    return answer

