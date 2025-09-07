import sys
from collections import deque

input = sys.stdin.readline

def parse_array(s: str):
    if s == "[]":
        return deque()
    # 대괄호 제거 후 분리
    body = s[1:-1]
    return deque(map(int, body.split(',')))

def main():
    t = int(input())
    out_lines = []

    for _ in range(t):
        p = input().strip()
        n = int(input())
        arr_str = input().strip()

        dq = parse_array(arr_str) if n > 0 else deque()
        rev = False
        error = False

        for cmd in p:
            if cmd == 'R':
                rev = not rev
            else:  # 'D'
                if not dq:
                    error = True
                    break
                if rev:
                    dq.pop()
                else:
                    dq.popleft()

        if error:
            out_lines.append("error")
        else:
            if rev:
                out_lines.append("[" + ",".join(map(str, reversed(dq))) + "]")
            else:
                out_lines.append("[" + ",".join(map(str, dq)) + "]")

    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
