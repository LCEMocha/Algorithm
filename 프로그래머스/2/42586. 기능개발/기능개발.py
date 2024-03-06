import math
def solution(progresses, speeds):
    day = []
    answer = []
    for i in range(len(progresses)):
        day.append(math.ceil((100-progresses[i])/speeds[i]))

    count = 1
    j = 0
    for i in range(1,len(day)):
        if day[j]>=day[i]:
            count += 1
            if i == len(day)-1:
                answer.append(count)
        else:
            answer.append(count)
            j = i
            count = 1
            if i == len(day)-1:
                answer.append(count)
    return answer
                   