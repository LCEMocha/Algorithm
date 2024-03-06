def solution(arr):
    li = []
    for i in range(1, len(arr)):
        if not li:
            li.append(arr[i-1])
        if arr[i-1] == arr[i]:
            continue
        else:
            li.append(arr[i])
    
    return li
            
            
    