from collections import deque

arr=list(input())
bomb=list(input())
li = []
for i in arr:
    li.append(i)
    if li[-len(bomb):] == bomb:
        del li[-len(bomb):]
if not li:
    print('FRULA')
else:
    print(''.join(li))